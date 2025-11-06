# Diretório do EP de Processamento de Lingua Natural

Este documento se propõe a dar uma explicação do código entregado e das tarefas desenvolvidas neste EP.

## Para avaliação rápida dos modelos de entrega

Os modelos da entrega do EP1 se encontram em:

- *EP1_best_arcaico_moderno.ipynb*: Entrega p/ dataset train_arcaico_moderno.csv
- *EP1_best_complexo_simples.ipynb*: Entrega p/ dataset train_complexo_simples.csv
- *EP1_best_literal_dinamico.ipynb*: Entrega p/ dataset train_literal_dinamico.csv

## Overview do projeto: Estrutura de diretórios

Além disso, os diretórios */Models/EP**N*** contém um subdiretório para cada instância de dados de treinamento do EP, e ainda cada um desses diretórios contém um subdiretório para cada modelo treinado. Além disso, cada um desses diretórios de modelos contém dois notebooks: Um com as pipelines de treinamento e outro com a execução do melhor modelo encontrado. Para compreender melhor, visualizemos: 


```
📁 Models/EP1
├── ArcaicoModerno           #Diretório com os modelos treinados p/ classificar em Arcaico/Moderno
    ├── LogisticRegression   #Treinamento de modelo Regressão Logística
        ├── model.ipynb          #Melhor modelo obtido à partir de pipeline.ipybn
        ├── pipeline.ipynb       #Pipelines de treinamento
    ├── NaiveBayes           #Treinamento de modelo Naive Bayes
        ├── model.ipynb
        ├── pipeline.ipynb
├── ComplexoSimples 
    ...
```

## Treinamento

### Modelos treinados

Nesta implementação, cada dataset foi treinado sobre os modelos LinearRegression e NaiveBayes. As pipelines de treinamento utilizam *k-best* para seleção de atributos, e fazem otimização de hiperparâmetros para cada modelo.

### Features geradas

As features trabalhadas neste EP em cada pipeline são:

1. Bag of Words
2. TF/TF-IDF
3. WORD NGrams
4. CHAR NGrams

## Geração dos modelos de entrega

 Configuradas as células das pipelines de treinamento, cada célula foi executada para encontrar os melhores parâmetros - pela utilização de ***GridSearchCV*** parâmetro de otimização *acurácia* e utilizando *10-fold cross validation*.
 
Logo, para cada dataset de treinamento da entrega, a pipeline de um modelo treinado para essa entrega produz uma parametrização *otimal* de cada modelo, e então comparamos a acurácia de cada modelo - para encontrar a melhor parametrização gerada para aquele dataset. Essa parametrização que se encontra nos notebooks *EP1_best_arcaico_moderno.ipynb*, *EP1_best_complexo_simples.ipynb* e *EP1_best_literal_dinamico.ipynb*.

**PS**: A parametrização não é realmente *otimal* porque em nenhum caso testamos todas parametrizações possiveis para nossos modelos, devido ao tempo/recursos dedicados. 


## Documentação Sugerida

A seguir estão algumas paginas de documentação utilizadas na construção desse EP:

1. Documentação da API do ScikitLearn: https://scikit-learn.org/stable/api/index.html
2. How to work with text data in ScikitLearn: https://scikit-learn.org/1.4/tutorial/text_analytics/working_with_text_data.html 