YES

Bon je me suis tapé une ptite barre, j'ai pondu deux trois trucs. Normalement ya des commentaires dans les fichiers, mais j'ajoute deux trois trucs ici.

J'ai tej tous les fichiers du dataset, parce que pas hyper utile de tous les avoir en ligne.

J'ai quand même foutu des fichiers pour que vous voyez mon arborescence de dataset (parce que spoiler, le script display.py ne marchera pas si tout est pas bien foutu au bon endroit).

J'ai aussi rename les fichiers qui contiennent les gaussiennes, parce que flemme de taper autant de caractères.

J'ai rename en Complexity_4G.txt, Complexity_8G.txt et Complexity_24G.txt, si vous voulez tout savoir.

# display.py:
  C'est le fichier pour faire la visualisation des signatures, pointillés toussa toussa.

  Rien de bien méchant, je me suis chaufé pour display 9 signatures, parce que why not

# main_v1.py:
  Là ya le bordel demandé dans la première partie

  Je fais un kmeans et un agglomerativeclustering

  J'ai l'impression que vous devez les implémenter, si c'est le cas bonne chance, moi perso flemme j'ai pris les fonctions de sklearn

  Pour le tsne, je sais pas si vous avez vu ça en cours, mais en gros c'est juste un algo qui projette votre mega dataset de 25 dimensions sur un espace en 2D, comme ça ensuite on peut visualiser l'effet du clustering
