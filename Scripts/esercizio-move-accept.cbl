      ******************************************************************
      * Author: Jordan
      * Date: 05/12/2023
      * Purpose: esercizio move-accept-display
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. esercizio.


       ENVIRONMENT DIVISION.

       CONFIGURATION SECTION.

       SPECIAL-NAMES.
       DECIMAL-POINT IS COMMA.

       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01  descrizione.
         02 nome PIC A(20).
         02 cognome PIC A(20).
         02 anno PIC ZZZ9.

       01  numero PIC 9(3).
       01  numero2 PIC ZZ9.9(2).

       01  persona.
         02 nome PIC A(7).
         02 cognome PIC A(7).
         02 videogioco PIC X(11).

       01  persona2.
         02 nome PIC A(6).
         02 cognome PIC A(6).
         02 videogioco PIC X(15).

       01  codicefiscale.
         02 nome PIC A(5).
         02 anno-nascita PIC 9(2).
         02 provincia PIC A(2).

       01  codicefiscale2.
         02 anno-nascita PIC 9(2).
         02 provincia PIC A(2).
         02 nome PIC a(5).

       01  str1.
         02 campo1 PIC 9(3).
         02 campo2 PIC X(5).
         02 campo3 PIC X(10).

       01  str2.
         02 campo1 PIC X(5).
         02 campo3 PIC X(10).
         02 campo2 PIC 9(3).


       PROCEDURE DIVISION.
       MAIN-PROCEDURE.

           MOVE "Gaetano" To nome IN descrizione.
           MOVE "Alessandrini" to cognome IN descrizione.
           MOVE 23 to anno IN descrizione.

           DISPLAY descrizione.
           MOVE 100 TO numero.
           MOVE 32 TO numero2.
           DISPLAY numero
           DISPLAY numero2


           DISPLAY "def1"
           PERFORM def1.

           DISPLAY "def2"
           PERFORM def2.

           DISPLAY "struttura1"
           PERFORM struttura1.

           DISPLAY "struttura2"
           PERFORM struttura2.

           STOP RUN.
           def1.
           MOVE "Franco" TO nome OF persona.
           MOVE " Verdi " TO cognome OF persona.
           MOVE "Super Mario" TO videogioco OF persona.
           DISPLAY nome IN persona NO ADVANCING.
           DISPLAY cognome IN persona NO ADVANCING.
           DISPLAY videogioco IN persona.

           def2.
           MOVE "Maria " TO nome OF persona2.
           MOVE "Viola " TO cognome OF persona2.
           MOVE "God of War" TO videogioco OF persona2.
           DISPLAY nome IN persona2 NO ADVANCING.
           DISPLAY cognome IN persona2 NO ADVANCING.
           DISPLAY videogioco IN persona2.


           MOVE "Banco" TO nome OF codicefiscale.
           MOVE 76 TO anno-nascita OF codicefiscale.
           MOVE "MI" TO provincia OF codicefiscale.

           DISPLAY nome in codicefiscale.
           DISPLAY anno-nascita in codicefiscale.
           DISPLAY provincia in codicefiscale.

           MOVE CORRESPONDING codicefiscale TO codicefiscale2
           DISPLAY nome in codicefiscale2 SPACE anno-nascita in
           codicefiscale2 SPACE provincia in codicefiscale2.

           struttura1.
           MOVE 123 TO campo1 of str1.
           MOVE "corso" TO campo2 OF str1.
           MOVE "cobol" TO campo3 OF str1.
           DISPLAY str1.

           struttura2.
           MOVE CORRESPONDING str1 TO str2.




       END PROGRAM esercizio.
