"""
Nom : Nieto Navarrete
Prenom : Matias
Matricule : 502920

Projet INFO-F103 : La startup EOL

Le programme se lance avec la ligne de commande : python3 binary_eol.py <fichier>
Pour le choix de la cible, elle se fait directement sur le terminal grace a un input. (ligne 514)

"""

import sys

class BinaryTree:
    """ Cree un arbre binaire. """
    def __init__(self, item=None):
        self.info = item
        self.left = None
        self.right = None
        self.father = None

    def set_root(self, item):
        self.info = item

    def set_left(self, item):
        self.left = BinaryTree(item)

    def set_right(self, item):
        self.right = BinaryTree(item)

    def get_root(self):
        return self.info

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def get_global_root(self):
        res = self
        if res != None:
            while res.father != None:
                res = res.father
        return res

    def find_element(self, arbre, element, res):
        """
        Cherche l'element dans l'arbre et renvoi l'element sous forme d'objet de l'arbre
        :param arbre: l'arbre à parcourir
        :param element: element à rechercher
        :param res: True ou False pour continuer la recursion
        :return: le noeud qui correspond à l'element
        """
        if arbre.get_root() == element:
            return arbre
        if arbre.get_left_child() != None and res == False:
            res = self.find_element(arbre.get_left_child(), element, res)
        if arbre.get_right_child() != None and res == False:
            res = self.find_element(arbre.get_right_child(), element, res)
        return res

    def find_parent(self, arbre, element,res = False):
        """
        Cherche le parent de l'element dans l'arbre. Si l'element est la racine de l'arbre il renvoi un de ses fils
        :param arbre: l'arbre à parcourir
        :param element: element à rechercher
        :res: True ou False pour continuer la recursion
        :return: le noeud parent de l'element
        """
        if arbre.get_root() == element:
            if arbre.get_left_child() != None:
                if arbre.get_left_child().get_root() == 'A':
                    if arbre.get_right_child() != None:
                        return arbre.get_right_child()
                else:
                    if arbre.get_left_child() != None:
                        return arbre.get_left_child()

        if arbre.get_left_child() != None and res == False:
            if arbre.get_left_child().get_root() == element:
                return arbre
            res = self.find_parent(arbre.get_left_child(), element, res)
        if arbre.get_right_child() != None and res == False:
            if arbre.get_right_child().get_root() == element:
                return arbre
            res = self.find_parent(arbre.get_right_child(), element, res)
        return res

    def find_frere(self, element, arbre, res = False):
        """
        Cherche le frère de l'element dans l'arbre
        :param arbre: l'arbre à parcourir
        :param element: element à rechercher
        :res: True ou False pour continuer la recursion
        :return: le noeud frère de l'element
        """
        if arbre.get_root() == element:
            return

        if arbre.get_left_child() != None and res == False:
            if arbre.get_left_child().get_root() == element:
                if arbre.get_right_child() != None:
                    if arbre.get_right_child().get_root() == 'A':
                        return None
                    else:
                        return arbre.get_right_child()
            res = self.find_frere(element, arbre.get_left_child(), res)
        if arbre.get_right_child() != None and res == False:
            if arbre.get_right_child().get_root() == element:
                if arbre.get_left_child() != None:
                    if arbre.get_left_child().get_root() == 'A':
                        return None
                    else:
                        return arbre.get_left_child()
            res = self.find_frere(element, arbre.get_right_child(), res)
        return res

    def element_in(self, element):
        """renvoi True si element est dans l'arbre sinon False"""
        if self.get_root() == element:
            return True
        if self.get_left_child() != None:
            if self.get_left_child().element_in(element) == True:
                return True
        if self.get_right_child() != None:
            if self.get_right_child().element_in(element) == True:
                return True
        return False

    def verifie_allumer(self, arbre, res = True):
        """
        Verifie que tout l'arbre a comme valeur A et renvoi
        True si c'est le cas
        """
        if arbre != None:
            if arbre.get_root() != 'A':
                res = False
            else:
                res = self.verifie_allumer(arbre.get_left_child(), res)
                res = self.verifie_allumer(arbre.get_right_child(), res)

        return res

    # Methode qui affiche l'arbre ( Trouver sur https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python )
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.info
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.info
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.info
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.info
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u

# Pas eu besoin de l'utiliser
class Info:
    def __init__(self):
        self.profondeurGauche = 0
        self.profondeurDroite = 0
        self.contiens = False
        self.temps = -1


class Solution:
    """ Calcul le temps d'activation de toutes les eoliennes du parc. """

    resultat = 0

    def __init__(self):
        self.tree = BinaryTree()
        self.descente = False
        self.premiere = True # permet de verifier que la cible lors du premier appel à calculer_temp est bien une feuille qui existe
        self.allumer = [] # stock les element allumer pendant la recursion pour les afficher sur le terminal

    def condition_racine(self,arbre):
        """
        Active le noeud gauche de l'arbre si le droit est allumé ou inversement
        :param arbre: l'arbre a parcourir
        """
        if arbre != None and arbre.left != None and arbre.get_root() == 'A':
            if arbre.left.get_root() != 'A':
                self.resultat += arbre.left.get_root()
                self.allumer.append(arbre.left.get_root())
                arbre.left.set_root('A')

        if arbre != None and arbre.right != None and arbre.get_root() == 'A':
            if arbre.right.get_root() != 'A':
                self.resultat += arbre.right.get_root()
                self.allumer.append(arbre.right.get_root())
                arbre.right.set_root('A')

    def condition_monter(self,arbre):
        """
        Active le sous noeud gauche et/ou droit de l'arbre
        :param arbre: l'arbre a parcourir
        """
        if arbre != None:
            if arbre.get_root() == 'A':
                if arbre.right != None:
                    if arbre.right.get_root() != 'A':
                        self.resultat += arbre.right.get_root()
                        self.allumer.append(arbre.right.get_root())
                        arbre.right.set_root('A')
                if arbre.left != None:
                    if arbre.left.get_root() != 'A':
                        self.resultat += arbre.left.get_root()
                        self.allumer.append(arbre.left.get_root())
                        arbre.left.set_root('A')

    def fini_monter(self,fils_gauche,fils_droit,info):
        """
        Verifie que tout les noeuds sont bien activé lors de la monter sinon rappel calculer_temp()
        :param fils_gauche: le sous arbre gauche du noeud
        :param fils_droit: le sous arbre droit du noeud
        :param info: nformations supplementaires sur le noeud actuel
        """
        fd_d,fd_g = self.valeur_fils(fils_droit)
        fg_d,fg_g = self.valeur_fils(fils_gauche)

        if fils_gauche != None or fils_droit != None:
            if fd_d != 'A' and fd_d != None:
                self.calculer_temps(fils_droit.right, info, fils_droit.right.get_root())

            elif fd_g != 'A' and fd_g != None:
                self.calculer_temps(fils_droit.left, info, fils_droit.left.get_root())

            elif fg_d != 'A' and fg_d != None:
                self.calculer_temps(fils_gauche.right, info, fils_gauche.right.get_root())

            elif fg_g != 'A' and fg_g != None:
                self.calculer_temps(fils_gauche.left, info, fils_gauche.left.get_root())

    def valeur_fils(self,fils):
        """
        Donne les valeur des enfants du fils si elles existent
        :param fils: le noeud acctuelle
        :return: valeur du fils droit et du fils gauche
        """
        f_d, f_g = None, None

        if fils!= None:
            if fils.right != None:
                f_d = fils.right.get_root()
            if fils.left != None:
                f_g = fils.left.get_root()

        return f_d,f_g

    def affche_allumage(self):
        """
        Affiche sur le terminal quel noeud s'allume avant chaque nouvelle recursion dans calculer_temps
        """
        print("\n")
        if len(self.allumer) > 1:
            print(f"T = {self.resultat - self.allumer[1]}s et T = {self.resultat}s (respec.) : les eoliennes {self.allumer[0]} et {self.allumer[1]} s’activent.")

        elif len(self.allumer) == 1:
            print(f"T= {self.resultat}s : l’eolienne {self.allumer[0]} s’active.")

        self.tree.display()

    def calculer_temps(self, noeud, info, cible):
        """
        Calcul le temps pour allumer chaque eolienne du parc.
        :param noeud: noeud actuel
        :param info: informations supplémentaires sur le noeud actuel
        :param cible: le noeud qui est activé
        :return: info
        """
        self.allumer = []

        # Condition pour qu'il commence que par une feuille
        if self.premiere:
            if not self.tree.element_in(cible):
                print("La cible demandée ne fait pas partie de l'arbre.")
                sys.exit(1)
            elif noeud.left != None or noeud.right != None:
                print("La cible demandée n'est pas une feuille.")
                sys.exit(1)

        # Descente
        if self.descente:

            # Cree enfant et le frere du noeud
            if noeud.left != None:
                enfant = noeud.left
            else:
                enfant = noeud.right
            frere = self.tree.find_frere(cible,self.tree)

            # Rajoute son temp dans resultat et allume la cible
            self.resultat += cible
            noeud.set_root('A')
            self.allumer.append(cible)

            # verifie si le noeud a un frere et l'active
            if frere != None :
                self.resultat += frere.get_root()
                self.allumer.append(frere.get_root())
                frere.set_root('A')

            self.affche_allumage()

            # condition arret
            if self.tree.verifie_allumer(self.tree):
                return info
            else:
                # continue la descente en prenant à chaque fois un des 2 enfants du noeud
                if enfant != None:
                    self.calculer_temps(enfant, self.tree, enfant.get_root())

                # reviens sur un noeud qui n'a pas ete activé
                if frere != None:
                    if frere.get_right_child() != None:
                        self.calculer_temps(frere.right, self.tree, frere.right.get_root())
                    elif frere.get_left_child() != None:
                        self.calculer_temps(frere.left, self.tree, frere.left.get_root())

        # Monter
        else:
            self.premiere = False # Déscative la condition pour qu'il commence par une feuille (permet d'avoir une feuille à 0)
            # cree pere, fils droit et fils gauche du noeud
            pere = self.tree.find_parent(self.tree, cible)
            fils_droit = noeud.get_right_child()
            fils_gauche = noeud.get_left_child()

            # verifie que le noeud n'est pas la racine de l'arbre
            if noeud.get_root() != self.tree.get_root():
                noeud.set_root('A')
                self.resultat += cible
                self.allumer.append(cible)

                self.condition_monter(fils_droit)
                self.condition_monter(fils_gauche)

                self.affche_allumage()

                self.calculer_temps(pere, info, pere.get_root())

                self.fini_monter(fils_gauche,fils_droit,info)

            # Si le noeud correspond a la racine de l'arbre
            else:
                self.condition_racine(fils_droit)
                self.condition_racine(fils_gauche)

                self.resultat += cible
                noeud.set_root('A')
                self.allumer.append(cible)

                self.affche_allumage()

                # condition arret
                if self.tree.verifie_allumer(self.tree):
                    return info
                else:
                    self.descente = True # active la descente car on est arriver a la racine de l'arbre
                    if pere != None and pere != False:
                        self.calculer_temps(pere, info, pere.get_root())

        return info

    def solve(self, racine, cible):
        info = Info()
        self.calculer_temps(racine,info,cible)
        return self.resultat


def liste_fichier(fichier):
    """
    Cree une liste de liste ou chaque sous-liste correspond a un noeud de l'arbre
    :return: la liste des listes des noeuds
    """
    liste = []
    with open(fichier) as f:
        for line in f:
            l = [x.strip() for x in line.split(":")] # converti les lignes du fichier en liste
            liste.append(l)

    split_element_coller(liste,",")

    for i in range(len(liste)):
        for j in range(len(liste[i])):
            liste[i][j] = liste[i][j].strip() # retire tout les espace de la liste
        if len(liste[i]) == 1:
            del liste[i]

    convert_int(liste)

    return liste

def split_element_coller(liste,caractere):
    """

    :param liste: la liste des listes des noeuds à mofier
    :param caractere: carcetere a retire de la liste
    :return: la liste des listes des noeuds
    """
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if caractere in liste[i][j]:
                if j != 0:
                    temp = liste[i][j].split(caractere)
                    del liste[i][j]
                    liste[i] = liste[i] + temp
                else:
                    temp = liste[i][j].split(caractere)
                    del liste[i][j]
                    temp += liste[i]
                    liste[i] = temp

def convert_int(liste):
    """
    Convertie tout les element de la liste en entier
    :param liste: la liste des listes des noeuds à convertir
    :return: la liste des listes des noeuds
    """
    for i in range(len(liste)):
        for j in range(len(liste[i])):
            if liste[i][j] == 'None':
                liste[i][j] = None
            else:
                liste[i][j] = int(liste[i][j])

    return liste

def cree_arbre(racine, liste, premiere_racine, i = 0):
    """
    Cree l'arbre binaire d’une maniere recursive.
    :param racine: l'arbre au depart
    :param liste: la liste des listes des noeuds
    :param racine_avant: la racine de l'arbre
    :param i: entier qui commence à 0 pour pouvoir recuperer le premier noeud qui se trouve dans la liste
    """

    if i == len(liste):
        return racine

    if racine.get_root() == None:
        racine.set_root(liste[i][0])
        if liste[i][1] != None:
            racine.set_left(liste[i][1])
        if liste[i][2] != None:
            racine.set_right(liste[i][2])
        cree_arbre(racine, liste, premiere_racine, i+1)

    else:
        e_node = racine.find_element(premiere_racine, liste[i][0], False)
        if liste[i][1] != None:
            e_node.set_left(liste[i][1])
        if liste[i][2] != None:
            e_node.set_right(liste[i][2])
        cree_arbre(e_node, liste, premiere_racine, i+1)


if __name__ == '__main__':
    # Bout de code qui construit l'arbre donné en exemple dans l'énoncé.

    if len(sys.argv) < 2:
       print("Utilisation: python3 binary_eol.py <fichier> ", file=sys.stderr)
       sys.exit(1)
    fichier: str = sys.argv[1]

    liste = liste_fichier(fichier)

    s = Solution()
    cree_arbre(s.tree, liste, s.tree.get_global_root())

    print("Input :")
    s.tree.display()

    cible = int(input("Feuille initiale (cible) = "))
    noeud = s.tree.find_element(s.tree,cible,False) # correspond au noeud de la cible sous forme d'objet (noeud.get_root() = cible)
    print("Output :")
    print(f"au bout de {s.solve(noeud,cible)} secondes tout le parc est actif.\n")
