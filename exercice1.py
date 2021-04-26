
# exo 1, q1
def compte_sequences(fichier):

    with open(fichier, "r") as f:
        lignes = f.readlines()

    nombre_sequences = 0
    for ligne in lignes:
        if ligne.startswith(">"):
            nombre_sequences += 1
        
    return nombre_sequences


# exo 1, q2
def dico_fichier_multifasta(fichier):
    dico = {}

    with open(fichier, "r") as f:
        lignes = [ ligne.strip() for ligne in f.readlines() ]

    for i in range(len(lignes)):
        identifiant = lignes[i]
        if identifiant.startswith(">"):
            sequence = lignes[i+1]
            dico.update({
                identifiant.replace(">", ""): sequence
            })

    return dico

# exo 1, q3
def taille_des_sequences_multifasta(fichier):

    with open(fichier, "r") as f:
        lignes = [ ligne.strip() for ligne in f.readlines() ]

    tailles = []
    for i in range(len(lignes)):
        sequence = lignes[i]
        if not sequence.startswith(">"):
            tailles.append(len(sequence))
            

    tailles.sort()
    return tailles

# exo 1, q 4
def occurrences_aa(dico_fasta):
    acides_amines = list("ACDEFGHIKLMNPQRSTVWY")
    nombres = { aa: 0 for aa in acides_amines }

    for sequence in dico_fasta.values():
        for aa in sequence:
            if aa in nombres.keys():
                nombres[aa] += 1

    return nombres



if __name__ == "__main__":
    fichier = "Scer_CDS.pmultifasta"

    # exo 1, q1
    print(compte_sequences(fichier))

    # exo 1, q2
    dico_fasta = dico_fichier_multifasta(fichier)
    print(dico_fasta)

    # exo 1, q3
    tailles = taille_des_sequences_multifasta(fichier)
    print(tailles)

    # exo 1, q 4
    aas = occurrences_aa(dico_fasta)
    print(aas)
