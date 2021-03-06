��          �            h  �   i  �   #  z   �  &   T  �   {  �   ^  �   �     u     �     �     �     �     �     �  �  �  �   �  �   �  �   N	  6   
    :
  �   I  �   �     �     �  
   �     �     �  %   �                    	                                                         
        
Default data serialization format is
<a href="http://en.wikipedia.org/wiki/JSON">JSON</a>, 
but you can also use XML by appending <code>?format=xml</code>
query parameter to each URL.
 
Each element of those lists contains a link (in a "href") attibute
which points to individual resource's details, i.e.:
<a href="%(e1)s">%(e1)s</a> or
<a href="%(e2)s">%(e2)s</a>.
 
If you only want top-level books and not all the children, you can use /parent_books/, as in:
<a href="%(e)s">%(e)s</a>.
 
The URLs in WolneLektury.pl API are:
 
The same way, using also books and themes, you can search for a list of fragments:
<a href="%(e)s">%(e)s</a>. 
Again, each entry has a "href" attribute which links to the fragment's details, i.e.:
<a href="%(f)s">%(f)s</a>. 
 
WolneLektury.pl API resides under <code>%(u)s</code>.
You can use it to access information about books, their fragments and
their metadata.
 
You can combine authors, epochs, genres and kinds to find only books matching
those criteria. For instance:
<a href="%(e)s">%(e)s</a>.
 List of all authors List of all books List of all epochs List of all genres List of all kinds List of all themes WolneLektury.pl API Project-Id-Version: PACKAGE VERSION
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2012-03-20 12:49+0100
PO-Revision-Date: 2012-03-20 12:50+0100
Last-Translator: Radek Czajka <radoslaw.czajka@nowoczesnapolska.org.pl>
Language-Team: LANGUAGE <LL@li.org>
Language: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=3; plural=(n==1 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
 
Dane domyślnie są serializowane w formacie <a href="http://pl.wikipedia.org/wiki/JSON">JSON</a>,
ale dostępny jest też format XML – wystarczy dodać parametr <code>?format=xml</code>
do każdego zapytania.
 
Każdy element na tych listach zawiera adres (w atrybucie „href”), pod którym można znaleźć szczegółowe dane, np. <a href="%(e1)s">%(e1)s</a> czy <a href="%(e2)s">%(e2)s</a>.
 
Aby spośród wszystkich pasujących wybrać tylko utwory najwyższego poziomu (pomijając ich podutwory), można użyć zapytania /parent_books/, np.: <a href="%(e)s">%(e)s</a>.
 
API Wolnych Lektur zawiera następujące adresy URL:
 
W ten sam sposób, filtrując dodatkowo według lektur lub motywów, można wyszukiwać fragmenty:<a href="%(e)s">%(e)s</a>. 
Każdy element uzyskanej listy w atrybucie „href” zawiera link do szczegółowego opisu danego fragmentu, np.:
<a href="%(f)s">%(f)s</a>. 
 
API serwisu WolneLektury.pl znajduje się pod adresem <code>%(u)s</code>.
Za jego pomocą można uzyskać informacje o utworach, ich fragmentach i metadanych.
 
Można łączyć autorów, epoki, gatunki i rodzaje, aby wybrać tylko utwory odpowiadające zadanym kryteriom. Na przykład: <a href="%(e)s">%(e)s</a>.
 Lista autorów Lista utworów Lista epok Lista gatunków literackich Lista rodzajów literackich Lista motywów i tematów literackich API serwisu WolneLektury.pl 