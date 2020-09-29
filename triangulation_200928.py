#!/usr/bin/env python3

import itertools
import numpy as np


def triangulate_unit_cube(n, k):

    """freudethal triangulation
       n: 立方体の次元
       k: chainの長さ

    """

    I = (0,1)

    #n次元立方体の全ての頂点のリスト
    position_list = list(itertools.product(I, repeat = n))

    #TODO ここはnが大きくなるとメモリ使用量が爆発するのでリストは使わない
    #position_listからk個の頂点を選んだ組み合わせのリスト
    #chain_candidate_iterator[p][q][r]=p番目のchain候補のq番目の頂点のr番目の要素
    chain_candidate_iterator = itertools.combinations(position_list, k)
    #print(chain_candidate_iterator)
    
    chain_list = []
    


    for chain_candidate in chain_candidate_iterator:
        
        is_chain_list = True

        for q in range(k - 1):
        
            for r in range(n):

                if not (chain_candidate[q][r] <= chain_candidate[q + 1][r]):
                    
                    #chain_candidate[q]とchain_candidate[q +  1]のr番目の要素について、前者が後者以下ならchainにならない

                    is_chain_list = False
                    break
                    
            if not is_chain_list:
                break
                
        if is_chain_list:
            
            chain_list.append(chain_candidate)
    
    
    return chain_list
    
#triangulate_unit_cube(3, 4)
#print(triangulate_unit_cube(3, 4))



def triangulate_grid(cube_position):
    dimension = len(cube_position)
    
    triangulate_unit_cube_array = np.array(triangulate_unit_cube(dimension, dimension + 1))
    cube_position_array = np.array(cube_position)
    
    triangulate_grid_array = triangulate_unit_cube_array + cube_position_array
                
    return triangulate_grid_array     
                
    
print(triangulate_grid([1, 0]))
print(triangulate_grid([0, 1]))
print(triangulate_grid([0, 0, 0]))
print(triangulate_grid([0, 0, 1]))

