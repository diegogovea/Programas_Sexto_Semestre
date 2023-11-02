/*Autor: Diego Leon Govea Ortiz
Materia: Seminario estructura de Datos
Actividad 02: Cadenas*/
#include<iostream>

using namespace std;

void ImprimeVertical(char*);

void ImprimeVertical(char* pszCadena){
    int i;
    for(i=0;pszCadena[i]!=NULL;i++){
        cout<<pszCadena[i]<<endl;
    }
}

main(){
    char frase[]="Diego Leon";
    ImprimeVertical(frase);

}
