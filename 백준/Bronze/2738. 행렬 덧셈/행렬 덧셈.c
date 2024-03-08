#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#pragma warning(disable:4996)

int main(void) {
	int N, M, num[100][100], num2[100][100] ,result[100][100];

	scanf("%d %d", &N, &M);
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			scanf("%d", &num[i][j]);
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			scanf("%d", &num2[i][j]);
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++)
			result[i][j] = num[i][j] + num2[i][j];
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			printf("%d ", result[i][j]);
		}
		printf("\n");
	}

	return 0; 
}