from sklearn.metrics import confusion_matrix
import numpy as np
import itertools
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import roc_curve, auc, roc_auc_score

cm = confusion_matrix(np.argmax(y_valid, axis=1), np.argmax(y_pred, axis=1))

def plot_confusion_matrix(cm, classes,
                    normalize=True,
                    title='Confusion matrix',
                    cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

if normalize:
    cm = np.round(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], decimals=2)
    print("Normalized confusion matrix")
else:
    print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
             horizontalalignment="center",
            color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    
    cm_plot_labels = ['bed', 'fall', 'pickup', 'run', 'sitdown', 'standup', 'walk']
    plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix_BiLSTM')
    plt.savefig('plot_confusion_matrix.eps', dpi=300, format='eps')
    plt.show()

    target =  ['bed', 'fall', 'pickup', 'run', 'sitdown', 'standup', 'walk']

    

    # set plot figure size
    fig, c_ax = plt.subplots(1,1, figsize = (12, 8))

    # function for scoring roc auc score for multi-class
    def multiclass_roc_auc_score(y_valid, y_pred, average="macro"):
        lb = LabelBinarizer()
        lb.fit(y_valid)
        y_valid = lb.transform(y_valid)
        y_pred = lb.transform(y_pred)

        for (idx, c_label) in enumerate(target):
            fpr, tpr, _ = roc_curve(y_valid[:,idx].astype(int), y_pred[:,idx])
            c_ax.plot(fpr, tpr, label = '%s (AUC:%0.2f)'  % (c_label, auc(fpr, tpr)))
        c_ax.plot(fpr, fpr, 'b-', label = 'Random Guessing')
        return roc_auc_score(y_valid, y_pred, average=average)

    print('ROC AUC score:', multiclass_roc_auc_score(y_train, y_pred))

    # plt.plot(multiclass_roc_auc_score(y_train, y_pred))
    c_ax.legend()
    c_ax.set_xlabel('False Positive Rate')
    c_ax.set_ylabel('True Positive Rate')
    plt.savefig('AUC_score.eps', dpi=300, format='eps')
    plt.show()
