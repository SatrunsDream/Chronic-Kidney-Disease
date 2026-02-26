"""
Generate Plotly HTML assets for the Chronic Kidney Disease storyboard site.
Run from repo root: python scripts/generate_assets.py
Writes to docs/assets/ (README filenames).
"""
import os
import sys
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.subplots as sp
import plotly.graph_objects as go
import plotly.figure_factory as ff
import scipy.stats as stats
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, auc
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_DIR = os.path.join(REPO_ROOT, 'data')
ASSETS_DIR = os.path.join(REPO_ROOT, 'docs', 'assets')
os.makedirs(ASSETS_DIR, exist_ok=True)

def main():
    os.chdir(REPO_ROOT)
    np.random.seed(42)

    # Load and parse column names from data_description.txt
    with open(os.path.join(DATA_DIR, 'data_description.txt'), 'r') as f:
        lines = f.readlines()
    col_names = [line.split('-', 1)[1].strip() for line in lines[1:]]
    df = pd.read_csv(os.path.join(DATA_DIR, 'kidney_disease.csv'))
    df.columns = col_names

    # Clean dtypes
    for feature in ['red blood cell count', 'packed cell volume', 'white blood cell count']:
        df[feature] = pd.to_numeric(df[feature], errors='coerce')
    df.drop(['id'], axis=1, inplace=True)

    def extract_cat_num(d):
        cat = [c for c in d.columns if d[c].dtype == 'object']
        num = [c for c in d.columns if d[c].dtype != 'object']
        return cat, num

    cat_col, num_cols = extract_cat_num(df)
    df['diabetes mellitus'] = df['diabetes mellitus'].replace({'\tno': 'no', '\tyes': 'yes', ' yes': 'yes'})
    df['coronary artery disease'] = df['coronary artery disease'].replace(to_replace='\tno', value='no')
    df['class'] = df['class'].replace(to_replace='ckd\t', value='ckd')

    # 1. Numeric histograms
    fig = sp.make_subplots(rows=5, cols=3, subplot_titles=num_cols)
    for i, feature in enumerate(num_cols):
        row, col = (i // 3) + 1, (i % 3) + 1
        fig.add_trace(go.Histogram(x=df[feature], nbinsx=30, name=feature, marker=dict(color='rgba(100, 100, 255, 0.7)')), row=row, col=col)
    fig.update_layout(height=1200, width=1800, showlegend=False, margin=dict(l=20, r=20, t=40, b=20), bargap=0)
    for i in range(1, 6):
        for j in range(1, 4):
            fig.update_xaxes(row=i, col=j, showgrid=False, zeroline=False, title_text="")
            fig.update_yaxes(row=i, col=j, showgrid=True, zeroline=False)
    fig.write_html(os.path.join(ASSETS_DIR, 'features_distribution_plot.html'))

    # 2. Categorical bars
    color_palette = ['rgba(100, 149, 237, 0.7)', 'rgba(255, 99, 71, 0.7)']
    fig = sp.make_subplots(rows=4, cols=3, subplot_titles=cat_col)
    for i, feature in enumerate(cat_col):
        row, col = (i // 3) + 1, (i % 3) + 1
        counts = df[feature].value_counts()
        colors = [color_palette[j % 2] for j in range(len(counts))]
        fig.add_trace(go.Bar(x=counts.index, y=counts.values, name=feature, marker=dict(color=colors)), row=row, col=col)
    fig.update_layout(height=1200, width=1200, showlegend=False, margin=dict(l=20, r=20, t=40, b=20))
    for i in range(1, 5):
        for j in range(1, 4):
            fig.update_xaxes(row=i, col=j, showgrid=False, zeroline=False)
            fig.update_yaxes(row=i, col=j, showgrid=True, zeroline=False)
    fig.write_html(os.path.join(ASSETS_DIR, 'features_distribution2_plot.html'))

    # 3. Correlation heatmap
    numeric_df = df.select_dtypes(include=[np.floating, np.integer])
    corr_df = numeric_df.corr()
    fig = go.Figure(data=go.Heatmap(z=corr_df.values, x=corr_df.columns, y=corr_df.columns, colorscale='Viridis', zmin=-1, zmax=1))
    for i in range(len(corr_df)):
        for j in range(len(corr_df.columns)):
            fig.add_annotation(x=corr_df.columns[j], y=corr_df.columns[i], text=str(round(corr_df.iloc[i, j], 2)),
                              showarrow=False, font=dict(color="white" if abs(corr_df.iloc[i, j]) < 0.5 else "black"))
    fig.update_layout(title="Correlation Heatmap", xaxis_nticks=36, width=800, height=800)
    fig.write_html(os.path.join(ASSETS_DIR, 'features_heat_map.html'))

    # 4. Violins by class
    fig = sp.make_subplots(rows=(len(num_cols) + 2) // 3, cols=3, subplot_titles=num_cols)
    for i, feature in enumerate(num_cols):
        row, col = (i // 3) + 1, (i % 3) + 1
        for class_value, color in zip(df["class"].unique(), ['red', 'blue']):
            subset = df[df["class"] == class_value]
            fig.add_trace(go.Violin(y=subset[feature], x=[class_value] * len(subset), name=f"{feature} - {class_value}",
                box_visible=True, meanline_visible=True, line_color="black", fillcolor=color, opacity=0.6), row=row, col=col)
    fig.update_layout(height=1200, width=1800, showlegend=False, margin=dict(l=20, r=20, t=40, b=20))
    fig.write_html(os.path.join(ASSETS_DIR, 'bivariate_class.html'))

    # 5. Density by class
    fig = sp.make_subplots(rows=(len(num_cols) + 2) // 3, cols=3, subplot_titles=num_cols)
    for i, feature in enumerate(num_cols):
        row, col = (i // 3) + 1, (i % 3) + 1
        for class_value, color in zip(df["class"].unique(), ['red', 'blue']):
            subset = df[df['class'] == class_value]
            fig.add_trace(go.Histogram(x=subset[feature], histnorm='density', name=class_value, marker_color=color,
                opacity=0.6, legendgroup=class_value, showlegend=(i == 0)), row=row, col=col)
        fig.update_xaxes(title_text=feature, row=row, col=col)
        fig.update_yaxes(title_text="Density", row=row, col=col)
    fig.update_layout(height=1200, width=1800, showlegend=True, legend_title="Class", title_x=0.5, margin=dict(l=20, r=20, t=40, b=20))
    fig.write_html(os.path.join(ASSETS_DIR, 'bivariate_class2.html'))

    # 6. Bivariate scatter grid
    cols = ["serum creatinine", "haemoglobin", "blood urea", "albumin", "red blood cell count", "packed cell volume"]
    fig = sp.make_subplots(rows=(len(cols) * (len(cols) - 1)) // 2 // 3 + 1, cols=3,
                          subplot_titles=[f'{x} vs {y}' for i, x in enumerate(cols) for y in cols[i+1:]])
    class_colors = {k: v for k, v in zip(df["class"].unique(), ['red', 'blue'])}
    subplot_index = 0
    for i, col1 in enumerate(cols):
        for col2 in cols[i+1:]:
            row, col = (subplot_index // 3) + 1, (subplot_index % 3) + 1
            for class_value, color in class_colors.items():
                subset = df[df['class'] == class_value]
                fig.add_trace(go.Scatter(x=subset[col1], y=subset[col2], mode='markers', marker=dict(color=color),
                    name=class_value, legendgroup=class_value, showlegend=(subplot_index == 0)), row=row, col=col)
            fig.update_xaxes(title_text=col1, row=row, col=col)
            fig.update_yaxes(title_text=col2, row=row, col=col)
            subplot_index += 1
    fig.update_layout(height=1200, width=1800, showlegend=True, legend_title="Class", title_x=0.5, margin=dict(l=20, r=20, t=40, b=20))
    fig.write_html(os.path.join(ASSETS_DIR, 'bivariate_class3.html'))

    # Imputation and encoding for modeling
    data = df.copy()
    def random_value_imputation(feature):
        n = data[feature].isnull().sum()
        if n == 0:
            return
        samp = data[feature].dropna().sample(n, random_state=42)
        samp.index = data[data[feature].isnull()].index
        data.loc[data[feature].isnull(), feature] = samp
    random_value_imputation('pus cell')
    random_value_imputation('red blood cells')
    for c in cat_col:
        data[c] = data[c].fillna(data[c].mode()[0])
    for c in num_cols:
        random_value_imputation(c)
    for c in cat_col:
        data[c] = LabelEncoder().fit_transform(data[c].astype(str))

    # Feature selection and split
    ind_col = [c for c in data.columns if c != 'class']
    X = data[ind_col]
    y = data['class']
    sel = SelectKBest(score_func=chi2, k=20).fit(X, y)
    scores = pd.DataFrame({'Features': X.columns, 'Score': sel.scores_})
    selected_columns = scores.nlargest(10, 'Score')['Features'].values
    X_new = data[selected_columns]
    X_train, X_test, y_train, y_test = train_test_split(X_new, y, train_size=0.75, random_state=42)

    labels = ['Class 0', 'Class 1']

    # 7. KNN confusion matrix
    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)
    cm = confusion_matrix(y_test, knn.predict(X_test))
    fig = ff.create_annotated_heatmap(z=cm, x=labels, y=labels, colorscale='Blues')
    fig.update_layout(title='Confusion Matrix', xaxis=dict(title='Predicted Labels'), yaxis=dict(title='True Labels'))
    fig.write_html(os.path.join(ASSETS_DIR, 'KNN_CM.html'))

    # 8. KNN ROC
    fpr, tpr, _ = roc_curve(y_test, knn.predict_proba(X_test)[:, 1])
    roc_auc = auc(fpr, tpr)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'ROC curve (area = {roc_auc:.2f})'))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Chance', line=dict(dash='dash')))
    fig.update_layout(title='Receiver Operating Characteristic', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
    fig.write_html(os.path.join(ASSETS_DIR, 'KNN_ROC.html'))

    # 9. RF confusion matrix
    rf = RandomForestClassifier()
    rs = RandomizedSearchCV(rf, param_distributions={"n_estimators": [100], "max_depth": [12], "min_samples_split": [5], "min_samples_leaf": [1], "max_features": [0.75], "criterion": ["gini"]}, n_iter=1, cv=2, random_state=42)
    rs.fit(X_train, y_train)
    best_rf = rs.best_estimator_
    best_rf.fit(X_train, y_train)
    cm = confusion_matrix(y_test, best_rf.predict(X_test))
    fig = ff.create_annotated_heatmap(z=cm, x=labels, y=labels, colorscale='Blues', showscale=True)
    fig.update_layout(title_text='Confusion Matrix', xaxis_title='Predicted Labels', yaxis_title='True Labels')
    fig.write_html(os.path.join(ASSETS_DIR, 'RFC_CM.html'))

    # 10. RF ROC
    fpr, tpr, _ = roc_curve(y_test, best_rf.predict_proba(X_test)[:, 1])
    roc_auc = auc(fpr, tpr)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'ROC curve (area = {roc_auc:.2f})'))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Chance', line=dict(dash='dash')))
    fig.update_layout(title='Receiver Operating Characteristic', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
    fig.write_html(os.path.join(ASSETS_DIR, 'RFC_ROC.html'))

    # 11. XGB confusion matrix
    xgb = XGBClassifier(objective='binary:logistic', use_label_encoder=False, eval_metric='logloss')
    rs = RandomizedSearchCV(xgb, param_distributions={"learning_rate": [0.25], "max_depth": [12], "min_child_weight": [1], "gamma": [0.1], "colsample_bytree": [0.3], "n_estimators": [100]}, n_iter=1, cv=2, random_state=42)
    rs.fit(X_train, y_train)
    best_xgb = rs.best_estimator_
    best_xgb.fit(X_train, y_train)
    cm = confusion_matrix(y_test, best_xgb.predict(X_test))
    fig_cm = ff.create_annotated_heatmap(z=cm, x=labels, y=labels, colorscale='Blues')
    fig_cm.update_layout(title='Confusion Matrix', xaxis=dict(title='Predicted Labels'), yaxis=dict(title='True Labels'))
    fig_cm.write_html(os.path.join(ASSETS_DIR, 'XGBC_CM.html'))

    # 12. XGB ROC
    fpr, tpr, _ = roc_curve(y_test, best_xgb.predict_proba(X_test)[:, 1])
    roc_auc = auc(fpr, tpr)
    fig_roc = go.Figure()
    fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name=f'ROC curve (area = {roc_auc:.2f})'))
    fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Chance', line=dict(dash='dash')))
    fig_roc.update_layout(title='Receiver Operating Characteristic', xaxis_title='False Positive Rate', yaxis_title='True Positive Rate')
    fig_roc.write_html(os.path.join(ASSETS_DIR, 'XGBC_ROC.html'))

    print("Generated 12 HTML assets in docs/assets/")

if __name__ == '__main__':
    main()
