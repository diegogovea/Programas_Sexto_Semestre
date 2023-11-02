/*Autor: Diego Leon Govea Ortiz
Materia: Seminario estructura de Datos
Actividad 02: Cadenas*/
#include<iostream>

using namespace std;

int Cuenta(char* pszCadena, char cContar);

int Cuenta(char* pszCadena, char cContar){
    int i,c=0;

    for(i=0;pszCadena[i]!=NULL;i++){
        cout<<pszCadena[i];
        if(pszCadena[i]==cContar)c++;
    }
    return c;
}

main(){
    char frase[]="Diego Leon";
    char cContar='e';
    cout<<endl<<Cuenta(frase,cContar);
}
