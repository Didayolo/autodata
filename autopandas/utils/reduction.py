# Dimensionality reduction functions

from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


def pca(data, key=None, verbose=False, **kwargs):
    """ Compute PCA.
        Use kwargs for additional PCA parameters (cf. sklearn doc).

        Parameters
        ----------
        key : Indexes key to select data.
        verbose : Display additional information during run.

        Returns
        -------
        AutoData
            Transformed data
    """
    pca = PCA(**kwargs)
    X = pca.fit_transform(data.get_data(key))
    if verbose:
        print('Explained variance ratio of the {} components: \n {}'.format(pca.n_components_,
                                                                            pca.explained_variance_ratio_))
        plt.bar(left=range(pca.n_components_),
                height=pca.explained_variance_ratio_,
                width=0.3,
                tick_label=range(pca.n_components_))
        plt.title('Explained variance ratio by principal component')
        plt.show()
    return X

def tsne(data, key=None, verbose=False, **kwargs):
    """ Compute T-SNE.
        Use kwargs for additional T-SNE parameters (cf. sklearn doc)

        Parameters
        ----------
        key : Indexes key to select data.
        verbose : Display additional information during run.

        Returns
        -------
        AutoData
            Transformed data
    """
    tsne = TSNE(**kwargs)
    X = tsne.fit_transform(data.get_data(key))
    return X

def lda(data, key=None, verbose=False, **kwargs):
    """ Compute Linear Discriminant Analysis.
        Use kwargs for additional LDA parameters (cf. sklearn doc)

        Parameters
        ----------
        key : Indexes key to select data.
        verbose : Display additional information during run.

        Returns
        -------
        AutoData
            Transformed data
    """
    lda = LinearDiscriminantAnalysis(**kwargs)
    X = data.get_data('X').get_data(key)
    y = data.get_data('y').get_data(key)
    if y.shape[1] > 1:
        raise Exception("LDA can't handle multi-output class. Use set_class method to define another target before calling lda.")
    X = lda.fit_transform(X, y)
    return X
