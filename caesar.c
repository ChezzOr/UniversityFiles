/*----------------------------------------------------------------
 *
 * Proyecto final: Cifrado con algoritmo cesar
 * Fecha: 26-Nov-2017
 *
 *--------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cheader.h"

#define WHEEL 25
#define SIZE 520000
#define TEXT 52

int main(int argc, char* argv[]){
	int i, j, k, z;
	double ms = 0.0;
	char * word;
	word = (char *) malloc(sizeof(char)*(SIZE+1));

	for (z = 0 ; z < 10000; z++){
		strncat(word ,"hola este texto esta cifrado con el algoritmo cesar ", TEXT);
	}

	for (k=0 ; k < N ; k++){
		start_timer();
		for (i = 0 ; i <= WHEEL ; i++){
			for (j=0 ; j < SIZE ; j++){
				if (word[j] <= 122 && word[j] >= 97){
					word[j] += 1;
					if (word[j] > 122){
						word[j] -= 26;
					}
				}
			}
			//printf("Rotated %i positions: %s \n", i+1, word);
		}
		ms += stop_timer();
	}
	
	printf("avg time = %f ms\n", ms/N);
	free(word);

	return 0;
}
