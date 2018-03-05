/*----------------------------------------------------------------
 *
 * Proyecto final: Cifrado con algoritmo cesar
 * Fecha: 26-Nov-2017
 *
 *--------------------------------------------------------------*/

import java.util.concurrent.RecursiveAction;

public class caesarForkJoin extends RecursiveAction{

	private int WHEEL;
	private int MIN = 10000_00;
	private char[] word;
	private int end, start;

	public caesarForkJoin(char[] text, int end, int start){
		this.word = text;
		this.start = start;
		this.end = end;
	}

	protected void computeDirectly(){
		for (int i=this.start ; i < this.end ; i++){
			if (word[start] <= 122 && word[start] >= 97){
				word[start] += 1;
				if (word[start] > 122){
					word[start] -= 26;
				}
			}
		}
	}

	@Override
	protected void compute(){
		if ( (this.end - this.start) <= this.MIN ) {
			this.computeDirectly();
		}else{
			int mid = (end + start) / 2;
			caesarForkJoin lowerMid = new caesarForkJoin(word, start, mid);
			lowerMid.fork();
			caesarForkJoin upperMid = new caesarForkJoin(word, mid, end);
			upperMid.compute();
			lowerMid.join();
		}
	}
}