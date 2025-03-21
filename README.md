Inteligenta artificiala 
Documentatie
Robu Victor Emanuel
Grupa 2
Mentor:Cosmin Fudulu 

Introducere:
Python este un limbaj de programare de nivel înalt, interpretat și ușor de utilizat, cunoscut pentru sintaxa sa clară și concisă. A fost lansat pentru prima dată în 1991. Python este folosit pe scară largă în dezvoltarea software-ului datorită versatilității sale și a unui ecosistem vast de biblioteci și module.
Utilizarile principale:
Dezvoltare web: Python poate fi folosit pentru a crea aplicații web folosind framework-uri precum Django și Flask. Aceste framework-uri facilitează gestionarea bazelor de date, autentificarea utilizatorilor și multe alte funcționalități ale aplicațiilor web.
Analiză de date: Python este extrem de popular în domeniul științei datelor, oferind biblioteci precum Pandas pentru manipularea datelor și Matplotlib pentru vizualizarea acestora.
Inteligență artificială și Machine Learning: Python este limbajul de alegere pentru cercetarea și dezvoltarea în domeniul inteligenței artificiale și machine learning, datorită bibliotecilor precum TensorFlow, Keras, scikit-learn și PyTorch.
Automatizare: Python este folosit pentru automatizarea unor sarcini repetitive, de la procesarea fișierelor text la interacțiunea cu API-uri și automatizarea testelor.
Aplicații desktop: Cu ajutorul bibliotecii Tkinter, Python poate fi folosit pentru a dezvolta aplicații grafice de birou, simple sau complexe.




Functionalitatea aplicatiei 
Acest cod creează o aplicație de genul feedback cu interfață grafică folosind tkinter. Utilizatorii pot vota pentru diferite niveluri de satisfacție (de la "Foarte Slab" la "Excelent"), iar aplicația actualizează și afișează numărul de voturi pentru fiecare categorie. Rezultatele sunt prezentate sub forma unui text care include numărul de voturi și o evaluare medie calculată pe baza acestora. Aplicația permite, de asemenea, adăugarea de comentarii,ce sunt salvate într-o zonă dedicate si vizibila. Evaluarea medie este afișată cu stele pentru a arata gradul de satisfacție global al utilizatorilor.
Ce face?
Aplicația funcționează astfel: când o persoană apasă pe un buton de vot, valoarea aferenta fiecărei categorii de satisfacție este incrementată. După fiecare vot, aplicația actualizează rezultatele, arătând numărul de voturi pentru fiecare opțiune și recalculând media generală a satisfacției. Media este calculată pe baza unui sistem ponderat, care acordă puncte diferite fiecărei opțiuni de vot. De asemenea, aplicația afișează aceste puncte sub formă de stele, pentru a oferi utilizatorului o reprezentare vizuală a evaluării medii. Utilizatorii pot adăuga comentarii, care sunt afișate într-o secțiune dedicată. Fiecare interacțiune este reflectată instantaneu în interfața utilizatorului.

Explicarea codului :

 
 
-Acesta este constructorul clasei feedback. Inițializează fereastra principală a aplicației, setează titlul acesteia și dimensiunea ferestrei.


 
-Facem un dicționar self.votes care va stoca numărul de voturi pentru fiecare categorie de feedback.           -Fiecare categorie începe cu valoarea 0.




 
 -Voting_frame este folosit pentru a pune toate butoanele de votare într-o secțiune a ferestrei.
 -Fiecare buton este asociat cu o funcție de votare specifică. 



De exemplu:
 
-Creăm un buton de vot pentru categoria „Foarte Slab”, care va apela funcția vote_foarte_slab atunci când este apăsat.

Dupa aceea avem:
 -results_frame conține informațiile referitoare la voturi), evaluarea medie și secțiunea de comentarii.


 
-calculăm media ponderată a voturilor. Fiecare categorie are o valoare asociată 
- Foarte Slab are 0.5, Excelent are 5).
-Media este calculată ca o sumă ponderată împărțită la numărul total de voturi
-Dacă nu există voturi ,se returnează 0.
 -Media este rotunjită la o zecimală.


 
-După calcularea mediei, afișăm evaluarea medie în stele (★ pentru stele pline și ☆ pentru stele goale).
-Stars_count este numărul de stele pline, iar restul stelelor sunt goale.


 
  -Când utilizatorul apasă butonul Adaugă Comentariu, se preia textul din comment_box si se adaugă în comments_display 
  -Comentariul este bagat în comments_display, iar caseta de comentarii este curățată pentru a permite introducerea unui nou comentariu.

 
-funcția vote_foarte_slab adaugă un vot pentru categoria Foarte Slab și actualizează rezultatele aplicației.


 
-După fiecare vot in parte, rezultatele și media sunt actualizate apelând funcțiile format_votes și update_average_label.


 
-Această funcție creează un șir de caractere care formatează rezultatele voturilor pentru a le afișa într-un mod clar și ușor de înțeles pe interfața grafică.


Afisarea grafica a aplicatiei:

 


