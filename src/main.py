import numpy as np
import time as time
import random
import os

matrix_main = []
sequences = []
combination = []
width = 0
height = 0

def intro():
    print("\n                             █▀▀ █▄█ █▄▄ █▀▀ █▀█   █▀█ █░█ █▄░█ █▄▀   ▀█ █▀█ ▀▀█ ▀▀█\n                             █▄▄ ░█░ █▄█ ██▄ █▀▄   █▀▀ █▄█ █░▀█ █░█   █▄ █▄█ ░░█ ░░█\n")
    print("██████╗░██████╗░███████╗░█████╗░░█████╗░██╗░░██╗  ██████╗░██████╗░░█████╗░████████╗░█████╗░░█████╗░░█████╗░██╗░░░░░\n██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██║░░██║  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░░░░░\n██████╦╝██████╔╝█████╗░░███████║██║░░╚═╝███████║  ██████╔╝██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░╚═╝██║░░██║██║░░░░░\n██╔══██╗██╔══██╗██╔══╝░░██╔══██║██║░░██╗██╔══██║  ██╔═══╝░██╔══██╗██║░░██║░░░██║░░░██║░░██║██║░░██╗██║░░██║██║░░░░░\n██████╦╝██║░░██║███████╗██║░░██║╚█████╔╝██║░░██║  ██║░░░░░██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝╚█████╔╝╚█████╔╝███████╗\n╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░░╚════╝░░╚════╝░╚══════╝")

def coorToToken(li):
    result = []
    for coor in li:
        result.append(matrix_main[coor[0]][coor[1]])
    return result

def getLastSubsetIdx(input_set, subset):
    # Nyari indeks kemunculan terakhir dari subset dalam set
    subset = subset[0]
    last_index = -1
    for i in range(len(input_set) - len(subset) + 1):
        if input_set[i:i + len(subset)] == subset:
            last_index = i + len(subset)
    
    return last_index

def optimizeSequence(lists, main):
    last = -1
    for list in lists:
        if (getLastSubsetIdx(coorToToken(main), list)> last):
            last = getLastSubsetIdx(coorToToken(main), list)

    if(last == -1):
        return main
    else:
        for i in range(len(main)-last):
            main.pop()
        return main

def generate_sequences(tokens, max_length):
    return random.choices(tokens, k= random.randint(2,max_length))

def generate_matrix(rows, cols, items):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.choice(items))
        matrix.append(row)
    return matrix

def getOccurrences(main_list, sublist):
    count = 0
    sublist_length = len(sublist)

    for i in range(len(main_list) - sublist_length + 1):
        if main_list[i:i + sublist_length] == sublist:
            count += 1
    return count

def getCombination(coor, urutan, vertical, n):
    urutan = urutan.copy()
    urutan.append(coor)
    if (n>1):
        if vertical:
            for i in range (height):
                if (not ([i,coor[1]] in urutan)):
                    getCombination([i,coor[1]], urutan, not vertical, n-1)
        else:
            for i in range (width):
                if (not ([coor[0],i] in urutan)):
                    getCombination([coor[0],i], urutan, not vertical, n-1)
    elif (n==1):
        combination.append(urutan)

def display_array(arr):
    return ' '.join(map(str, arr))

def print_matrix(matrix):
    for row in matrix:
        print("|", end=" ")
        print(" ".join(map(str, row)), end=" ")
        print("|")

def eliminate_after_subset(original_list, subset):
    subset_str = ''.join(subset)
    original_str = ''.join(original_list)
    subset_index = original_str.find(subset_str)
    if subset_index != -1:
        original_list = original_list[:subset_index + len(subset)]
    return original_list


def main():
    global matrix_main 
    global sequences 
    global combination 
    global width
    global height
    
    intro()
    type = int(input("Pilih Metode Input : \n1. File \n2. Command Line Interface \n(Ketik 1 atau 2)\n>> "))

    if (type == 1):
        nama_file = input("Masukkan nama file: \n>> ")
        # Looping mencari file
        while True:
            try:
                with open(f"../test/{nama_file}", "r") as file:
                    print("File ditemukan!")
                break 
            except FileNotFoundError:
                print("File tidak ditemukan. Coba lagi.")
            nama_file = input("Masukkan nama file: \n>> ")

        file = open(f"../test/{nama_file}", "r")

        # Buffer Size
        line = file.readline() 
        buffer = int(line)

        # Matrix size dan matrix handle
        line = file.readline()
        size = line.split()
        width = int(size[0])
        height = int(size[1])

        for i in range(height):
            elements_in_line = []
            line = file.readline()
            rows = line.split()
            for element in rows :
                elements_in_line.append(element) 
            matrix_main.append(elements_in_line)
        
        line = file.readline()
        total_sequence = int(line)
        for i in range(total_sequence):
            sequence = [] # hapus aja kalo ga bikin error
            line = file.readline()
            sequence = line.split()

            line = file.readline()
            reward  = int(line)
            sequences.append([sequence,reward])
        file.close()

    elif (type ==2):
        jumlah_token_unik = input("Jumlah token unik: \n>> ")
        token = input("Token: \n>> ") 
        token = token.split()
        buffer = int(input("Ukuran buffer: \n>> "))
        ukuran_matriks = input("Ukuran matrix (width height): \n>> ")
        jumlah_sekuens = int(input("Jumlah sekuens: \n>> "))
        ukuran_maksimal_sekuens = int(input("Ukuran maksimal sekuens: \n>> "))

        for i in range (jumlah_sekuens):
            sequences.append([generate_sequences(token,ukuran_maksimal_sekuens),random.randrange(10,101,10)])
        ukuran_matriks = ukuran_matriks.split()
        width = int(ukuran_matriks[0])
        height = int(ukuran_matriks[1])
        matrix_main = generate_matrix(height, width,token)
        
        print("\n====================================================")
        print("Generated Matrix:")
        print_matrix(matrix_main)
        print("\nGenerated Sequence:")
        for item in sequences:
            print(' - '.join(map(str, item[0])),":" ,item[1])

        print("====================================================")

    # Kalkulasi semua kemungkinan
    start =time.time()    

    for i in range(width):
        getCombination([0,i],[],True, buffer)

    max = [0,0]

    # Kalkulasi point terbesar
    for kombinasi in combination:
        count = 0
        for sekuens in sequences:
            count += sekuens[1]*getOccurrences(coorToToken(kombinasi),sekuens[0])
        if (count > max[1]):
            max = [kombinasi, count]
            # print("Updated max: ", max)

    max[0] = optimizeSequence(sequences, max[0]) 


    end = time.time()

    # Menampilkan Hasil
    print("\n======================result========================")
    if max[1]==0:
        print("0")
    else:
        print(max[1])
        for coor in max[0]:
            print(matrix_main[coor[0]][coor[1]], end = ' ')
        print()
        for coor in max[0]:
            print(f"{coor[1]+1}, {coor[0]+1}")
    print()
    print((end-start)*1000, "ms")
    print("====================================================")
    finish = input("Apakah ingin menyimpan solusi? (y/n) \n>> ")


    if finish == 'y':
        index = 1
        while True:
            os.chdir('../test')
            filename = f"output({index}).txt"
            if not os.path.exists(filename):
                with open(filename, 'w') as file:
                    if max[1] == 0:
                        file.write("0\n")
                    else:
                        file.write(str(max[1]))
                        file.write("\n")
                        for coor in max[0]:
                            file.write(str(matrix_main[coor[0]][coor[1]]) + ' ')
                        file.write("\n")
                        for coor in max[0]:
                            file.write(f"{coor[1]+1}, {coor[0]+1}\n")
                    file.write(f"{(end-start)*1000} ms")  
                break
            index += 1

main()