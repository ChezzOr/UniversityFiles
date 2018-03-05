/*----------------------------------------------------------------
 *
 * Proyecto final: Cifrado con algoritmo cesar
 * Fecha: 26-Nov-2017
 *
 *--------------------------------------------------------------*/

#include <iostream>
#include <tbb/task_scheduler_init.h>
#include <tbb/parallel_for.h>
#include <tbb/blocked_range.h>
#include "cppheader.h"

#define WHEEL 25
#define SIZE 520000
#define TEXT 52

using namespace std;
using namespace tbb;

const int GRAIN = 1000;

class Caesar{
private:
	char * word;

public:
	Caesar(char * w): word(w){}

	Caesar(Caesar &x, split): word(x.word){}

	void operator() (const blocked_range<int> &r) const {
		for (int j = r.begin(); j != r.end(); j++) {
			if (word[j] <= 122 && word[j] >= 97){
				word[j] += 1;
				if (word[j] > 122){
					word[j] -= 26;
				}
			}
		}
	} 
};

int main(int argc, char* argv[]){
	int i, k, z;
	double ms = 0.0;

	Timer t;

	char * word;
	word = (char *) malloc(sizeof(char)*(SIZE+1));

	for (z = 0 ; z < 10000; z++){
		strncat(word ,"hola este texto esta cifrado con el algoritmo cesar ", TEXT);
	}

	for (k=0 ; k < N ; k++){
		
		t.start();
		for (i = 0 ; i <= WHEEL ; i++){
			
			parallel_for( blocked_range<int>(0, SIZE, GRAIN), Caesar(word) );
			
			//printf("Rotated %i positions: %s \n", i+1, word);
		}
		ms += t.stop();
	}
	
	printf("avg time = %f ms\n", ms/N);
	free(word);

	return 0;
}
