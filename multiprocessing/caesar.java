/*----------------------------------------------------------------
 *
 * Proyecto final: Cifrado con algoritmo cesar
 * Fecha: 26-Nov-2017
 *
 *--------------------------------------------------------------*/

public class caesar{
	public static void main(String[] args){
		double ms = 0.0;
		int WHEEL = 25, N = 10;
		int TEXT = 520000;
		String text = "";

		for(int i = 0 ; i < 10000 ; i++){
			text = text.concat("hola este texto esta cifrado con el algoritmo cesar ");
		}

		char[] word;

		for (int k=0 ; k < N ; k++){
			word = text.toCharArray();
			double start = System.currentTimeMillis();
			for (int i = 0 ; i <= WHEEL ; i++){
				for (int j=0 ; j < TEXT ; j++){
					if (word[j] <= 122 && word[j] >= 97){
						word[j] += 1;
						if (word[j] > 122){
							word[j] -= 26;
						}
					}
				}
				//System.out.println("Rotated "+ i +" positions:" + new String(word));
			}
			ms += System.currentTimeMillis() - start;
		}
		System.out.println("avg time = " + ms/(double)N +" ms");
	}
}