      ******************************************************************
      * Author: jordan
      * Date: 05/12/2023
      * Purpose: esercizio di aritmetica
      * Tectonics: cobc
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. aritmetica.
       DATA DIVISION.
       FILE SECTION.
       WORKING-STORAGE SECTION.
       01  str1.
         02 num1 PIC 9(2) value 10.
         02 num2 PIC 9(2) value 12.

       01  str2.
         02 num1 PIC 9(2) value 15.
         02 num2 PIC 9(2) value 9.

       01  str3.
         02 num1 PIC 9(3).
         02 num2 PIC 9(3).

       01  eta PIC 9(2).
       01  partecipanti PIC 9(1).
       01  risultato PIC 9(3).

       01  eroe.
         02 nome PIC A(10).
         02 supereroe PIC A(20).
         02 eta2 PIC 9(4).

       01  anno-attuale PIC 9(4) value 2023.
       01  numero-vite PIC 9(2).



       PROCEDURE DIVISION.
       MAIN-PROCEDURE.
           MULTIPLY num1 IN str1 BY num1 IN str2 GIVING num1 IN str3
            ON SIZE ERROR DISPLAY "AHAAH!"
            NOT ON SIZE ERROR DISPLAY "r " num1 IN str3.

           MULTIPLY num2 IN str1 BY num2 IN str2 GIVING num2 IN str3
            ON SIZE ERROR DISPLAY "AHAAH!"
            NOT ON SIZE ERROR DISPLAY "r2 " num2 IN str3.

           DISPLAY "dammi un numero".
            ACCEPT num1 IN str1.
           DISPLAY "dammi un secondo numero".
            ACCEPT num1 IN str2.
           ADD num1 in str1 num1 in str2 TO num1 in str3.
           DISPLAY num1 in str3.
           DISPLAY "dammi un numero".
            ACCEPT num2 IN str1.
           DISPLAY "dammi un secondo numero".
            ACCEPT num2 IN str2.
           ADD num2 in str1 num2 in str2 TO num2 in str3.
           DISPLAY num2 in str3.
           COMPUTE num1 in str3 = num1 IN str1 + num1 in str2.
           COMPUTE num2 in str3 = num2 IN str1 + num2 in str2.


           SUBTRACT CORRESPONDING str1 FROM str2.
           DISPLAY str2.


           DISPLAY "qual'è la tua età?"
           ACCEPT eta.
           ACCEPT partecipanti.
           DIVIDE eta BY partecipanti GIVING risultato.
           DIVIDE risultato BY 0 giving risultato
           ON SIZE ERROR DISPLAY "no possible".

           DISPLAY "nome".
           ACCEPT nome.
           DISPLAY "ETA2".
           ACCEPT eta2 in eroe.
           SUBTRACT eta2 FROM anno-attuale GIVING eta2.
           DISPLAY "numero-vite salvate?"
           ACCEPT numero-vite.
           DIVIDE numero-vite BY eta2 GIVING numero-vite.



            STOP RUN.




       END PROGRAM aritmetica.
