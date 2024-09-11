from io import BytesIO
import base64
import matplotlib.pyplot as plt
import numpy as np

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(6, 3))
    
    if 'Name' in data.columns and 'Cooking Time' in data.columns:
        if chart_type == 'bar-chart':
            plt.bar(data['Name'], data['Cooking Time'])
        elif chart_type == 'pie-chart':
            plt.pie(data['Cooking Time'], labels=data['Name'], autopct='%1.1f%%')
        elif chart_type == 'line-chart':
            plt.plot(data['Name'], data['Cooking Time'])
        else:
            print('unknown chart type')
        
        plt.title(f'{chart_type.replace("-", " ").title()} of Cooking Times')
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time (minutes)')
    else:
        plt.text(0.5, 0.5, 'No data available', ha='center', va='center')
    
    plt.tight_layout()
    chart = get_graph()
    return chart

def rename_columns(df):
    column_mapping = {
        'name': 'Name',
        'cooking_time': 'Cooking Time',
        'ingredients': 'Ingredients',
        'difficulty': 'Difficulty'
    }
    return df.rename(columns=column_mapping)