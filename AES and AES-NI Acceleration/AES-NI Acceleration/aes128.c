
#include<stdio.h>
#include <stdint.h>     //for int8_t
#include <string.h>     //for memcmp
#include <wmmintrin.h>  //for intrinsics for AES-NI
//compile using gcc and following arguments: -g;-O0;-Wall;-msse2;-msse;-march=native;-maes

void encrypt(uint8_t* plainText, //pointer to the PLAINTEXT
	uint8_t* cipherText, //pointer to the CIPHERTEXT buffer
	__m128i* key_schedule) //pointer to the expanded key schedule
{
	__m128i tmp;
	int  j;
	tmp = _mm_loadu_si128((__m128i*)plainText);
	tmp = _mm_xor_si128(tmp, ((__m128i*)key_schedule)[0]);
	for (j = 1; j < 10; j++)
	{
		tmp = _mm_aesenc_si128(tmp, ((__m128i*)key_schedule)[j]);
	}
	tmp = _mm_aesenclast_si128(tmp, ((__m128i*)key_schedule)[10]);
	_mm_storeu_si128((((__m128i*)cipherText)), tmp);

}



void decrypt(uint8_t* cipherText, //pointer to the ciphertext
	uint8_t* plainText, //pointer to the plainText buffer
	__m128i* key_schedule) //pointer to the expanded key schedule
{
	__m128i tmp;
	int  j;
	tmp = _mm_loadu_si128((__m128i*)cipherText);
	tmp = _mm_xor_si128(tmp, ((__m128i*)key_schedule)[10]);

	for (j = 1; j < 10; j++)
	{
		tmp = _mm_aesdec_si128(tmp, ((__m128i*)key_schedule)[10 + j]);
	}
	tmp = _mm_aesdeclast_si128(tmp, ((__m128i*)key_schedule)[0]);
	_mm_storeu_si128((((__m128i*)plainText)), tmp);


}


void Key_Expansion(uint8_t* userkey, __m128i* key)
{
	__m128i temp1, temp2;
	__m128i* Key_Schedule = (__m128i*)key;

	temp1 = _mm_loadu_si128((__m128i*)userkey);
	Key_Schedule[0] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x1);
	__m128i temp3;
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[1] = temp1;

	temp2 = _mm_aeskeygenassist_si128(temp1, 0x2);

	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);

	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[2] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x4);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[3] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x8);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[4] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x10);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[5] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x20);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[6] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x40);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[7] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x80);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[8] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x1b);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[9] = temp1;
	temp2 = _mm_aeskeygenassist_si128(temp1, 0x36);
	temp2 = _mm_shuffle_epi32(temp2, 0xff);
	temp3 = _mm_slli_si128(temp1, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp3 = _mm_slli_si128(temp3, 0x4);
	temp1 = _mm_xor_si128(temp1, temp3);
	temp1 = _mm_xor_si128(temp1, temp2);
	Key_Schedule[10] = temp1;

	Key_Schedule[19] = _mm_aesimc_si128(Key_Schedule[1]);
	Key_Schedule[18] = _mm_aesimc_si128(Key_Schedule[2]);
	Key_Schedule[17] = _mm_aesimc_si128(Key_Schedule[3]);
	Key_Schedule[16] = _mm_aesimc_si128(Key_Schedule[4]);
	Key_Schedule[15] = _mm_aesimc_si128(Key_Schedule[5]);
	Key_Schedule[14] = _mm_aesimc_si128(Key_Schedule[6]);
	Key_Schedule[13] = _mm_aesimc_si128(Key_Schedule[7]);
	Key_Schedule[12] = _mm_aesimc_si128(Key_Schedule[8]);
	Key_Schedule[11] = _mm_aesimc_si128(Key_Schedule[9]);
}


int main() {

	uint8_t plain[] = { 0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x33 };
	uint8_t key[] = { 0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c };
	uint8_t cipher[] = { 0x71,0x6b,0x46,0xe9,0x65,0x0d,0x74,0x22,0x46,0x7d,0x54,0xa0,0x60,0xa7,0xe4,0xa3 };
	uint8_t computed_plain[16];
	uint8_t computed_cipher[16];
	__m128i key_schedule[20];
	int i;
	Key_Expansion(key, key_schedule);
	encrypt(plain, computed_cipher, key_schedule);
	decrypt(cipher, computed_plain, key_schedule);

	for (i = 0; i < 16; i++)
	{
		printf("0x%02x,", computed_cipher[i]);
	}
	printf("\n");
	for (i = 0; i < 16; i++)
	{
		printf("0x%02x,", computed_plain[i]);
	}
	return 0;

}