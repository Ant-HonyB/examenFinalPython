from exercice1 import *
import pathlib

#exo2, q1
if __name__ == "__main__":
    fichier1 = ["Sarb_CDS.pmultifasta", "Sbay_CDS.pmultifasta", "Scer_CDS.pmultifasta", "Skud_CDS.pmultifasta", "Smik_CDS.pmultifasta", "Spar_CDS.pmultifasta"]
    fichier2 = ["Sarb_NCORFs.pmultifasta", "Sbay_NCORFs.pmultifasta", "Scer_NCORFs.pmultifasta", "Skud_NCORFs.pmultifasta", "Smik_NCORFs.pmultifasta", "Spar_NCORFs.pmultifasta"]

    fichier1 = pathlib.Path("FASTA_CDS")
    fichier2 = pathlib.Path("FASTA_NC")

    dico_fasta_CDS = {}
    dico_fasta_NC = {}
    tailles_CDS = []
    tailles_NC = []

    for i in fichier1.glob("*.pmultifasta"):
        dico_fasta_CDS.update(dico_fichier_multifasta(i))
        tailles_CDS.append(taille_des_sequences_multifasta(i))

    for i in fichier2.glob("*.pmultifasta"):
        dico_fasta_NC.update(dico_fichier_multifasta(i))
        tailles_NC.append(taille_des_sequences_multifasta(i))

    ensemble_tailles = tailles_CDS + dico_fasta_NC
    print(ensemble_tailles)
    print(dico_fasta_CDS)
    print(dico_fasta_NC)


