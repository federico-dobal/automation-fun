# Bugs found on Internet

## Case 1: atletismorosario.com

### Description

### Steps to reproduce the issue
1. Access to http://www.atletismorosario.com.ar/

2. Click in menu option _Maratones_

3. Click in menu option _Resultados_
![Alt text](resources/atletismo/menu_option.png?raw=true )

4. Click in link _VILLA GOBERNADOR GALVEZ CORRE_
![Alt text](resources/atletismo/link_VGG.png?raw=true )

5. Change url id to for instance 999
![Alt text](resources/atletismo/url_id.png?raw=true )

### Current behaviour
Error message is shown on the page:
![Alt text](resources/atletismo/error.png?raw=true )

### Expected behaviour
Not found page message should be shown properly. At least the error message should not be shown to the user. 

## Case 2: getinkspired.com

### Description
Translations do not work fully consistently. 

For instance, when accessing the page _Conseils pour écrire (Blog)_, it is not completelly translated into French, Actually most of the page is in English, however there are still links in French.

### Steps to reproduce the issue
1. Access https://getinkspired.com/fr/

2. Click in the menu option _Auteurs & creators_
    

3. Click in the sub menu option _Conseils pour écrire (Blog)_
![Alt text](resources/ink/menu_option.png?raw=true )


### Current behaviour
The page is mostly in English except some links that are in French(as expected):
![Alt text](resources/ink/bug.png?raw=true ) 

### Expected behaviour 
Since we are accessing to /fr subdomain, the expected behavior is the full page to be in French.