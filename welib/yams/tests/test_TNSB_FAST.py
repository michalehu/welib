import unittest
import numpy as np

from welib.yams.TNSB_FAST import *

MyDir=os.path.dirname(__file__)

class TestTNSB(unittest.TestCase):
    def test_TNSB_FAST(self):

        bStiffening=True
        nShapes_twr=2
        nShapes_bld=0
        nDOF = 1 + nShapes_twr + nShapes_bld * 3
        q = np.zeros((nDOF,1)) # TODO, full account of q not done
        q[[0]]=1
        q[[1]]=0.1
        q[[2]]=0*np.pi/4.

        np.set_printoptions(linewidth=500)
        EDFile = os.path.join(MyDir, '../../../_data/NREL5MW/data/NREL5MW_ED.dat')

        # --- Auto assembly with z axis
        main_axis='z'
        assembly='auto'

        StructA= FASTmodel2TNSB(EDFile, nShapes_twr=nShapes_twr,nShapes_bld=nShapes_bld, DEBUG=False, assembly=assembly , q=q, main_axis=main_axis, bStiffening=bStiffening)

        # --- Manual assembly with x axis
        assembly='auto'
        main_axis='x'
        StructM= FASTmodel2TNSB(EDFile, nShapes_twr=nShapes_twr,nShapes_bld=nShapes_bld, DEBUG=False, assembly=assembly , q=q, main_axis=main_axis, bStiffening=bStiffening)


        # --------------------------------------------------------------------------------}
        # --- Components
        # --------------------------------------------------------------------------------{
        #  from scipy.linalg import block_diag
        ##     print('RR')
        #     RR = np.eye(3)
        #     RR = np.zeros((3,3))
        #     RR[0,2]=1 # send z to x
        #     RR[1,1]=-1 # send y to -y
        #     RR[2,0]=1  # send x to z
        #     RR=block_diag(RR,RR)
        #     print(RR)

        # --- Tower
        Twr_MMref= np.array([[ 3.07795822e+05,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.04093341e+07, -0.00000000e+00 , 8.43721581e+04, -2.21926938e+06],
                             [ 0.00000000e+00,  3.07795822e+05,  0.00000000e+00, -1.04093341e+07,  0.00000000e+00,  0.00000000e+00 , 0.00000000e+00,  0.00000000e+00],
                             [ 0.00000000e+00,  0.00000000e+00,  3.07795822e+05,  0.00000000e+00, -0.00000000e+00,  0.00000000e+00 , 0.00000000e+00,  0.00000000e+00],
                             [ 0.00000000e+00, -1.04093341e+07,  0.00000000e+00,  5.00392913e+08, -0.00000000e+00, -0.00000000e+00 , 0.00000000e+00,  0.00000000e+00],
                             [ 1.04093341e+07,  0.00000000e+00, -0.00000000e+00, -0.00000000e+00,  5.00392913e+08, -0.00000000e+00 , 1.44671171e+12, -2.94821305e+13],
                             [-0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -0.00000000e+00, -0.00000000e+00,  0.00000000e+00 , 0.00000000e+00,  0.00000000e+00],
                             [ 8.43721581e+04,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00,  1.44671171e+12,  0.00000000e+00 , 4.78239541e+04, -7.83818828e+05],
                             [-2.21926938e+06,  0.00000000e+00,  0.00000000e+00,  0.00000000e+00, -2.94821305e+13,  0.00000000e+00 ,-7.83818828e+05,  2.41136381e+07]])
        np.testing.assert_almost_equal(StructA.Twr.r_O.ravel(), (0,0,10))
        np.testing.assert_almost_equal(StructA.Twr.MM[:6,:6]/1e5, Twr_MMref[:6,:6]/1e5, 5)
        np.testing.assert_almost_equal(StructA.Twr.MM[6:,:]/1e10, Twr_MMref[6:,:]/1e10, 5)
        np.testing.assert_almost_equal(StructA.alpha.ravel(), (0,0.1194396,0))
        # print('Twr: B_T:')
        # print(StructA.Twr.B_inB)
        # print(StructM.Twr.B_inB)
        # print(StructA.Twr.r_O)
        # print(StructM.Twr.r_O)
        # print(StructA.Twr.Mass)
        # print(StructA.Twr.MM)
        # print(StructA.Twr.r_O)
        # print('Twr.alpha_y:')
        # print(StructA.alpha)
        # print(StructM.alpha)
        # print('Twr Damp matrix:')
        # print(StructA.Twr.DD)
        # print(StructM.Twr.DD)
        # print('Twr KK matrix:')
        # print(StructA.Twr.KK)
        # print(StructM.Twr.KK)
        # print('Twr Mass matrix:')
        # print(StructA.Twr.MM[6:,6:])
        # print(StructM.Twr.MM[6:,6:])
        # print(StructA.Twr.MM[6:,6:]-StructM.Twr.MM[6:,6:])

        # --- Nacelle
        Nac_MMref= np.array([[ 240000.,       0.,       0. ,      0.,  420000.,      -0.],
                             [      0.,  240000.,       0. ,-420000.,       0.,  456000.],
                             [      0.,       0.,  240000. ,      0., -456000.,       0.],
                             [      0., -420000.,       0. ,      0.,       0.,       0.],
                             [ 420000.,       0., -456000. ,      0.,       0.,       0.],
                             [     -0.,  456000.,       0. ,      0.,       0., 2607890.]])
        np.testing.assert_almost_equal(StructA.Nac.Mass, 240000)
        np.testing.assert_almost_equal(StructA.Nac.r_O.ravel(),(0,0,87.6))
        np.testing.assert_almost_equal(StructA.Nac.MM,Nac_MMref)
        # print(StructA.Nac.Mass)
        # print(StructA.Nac.MM)
        # print(StructA.Nac.r_O)
        # print('Nac: B_N:')
        # print(StructM.Nac.B_inB)
        # print(np.dot(RR, StructA.Nac.B_inB))
        # print('Nac R_B:')
        # print(StructA.Nac.R_0b)
        # print(StructM.Nac.R_0b)
        
        # --- Shaft
        Sft_MMref=np.array([[  56780.    ,         0.      ,       0.    ,         0.    ,         0.       ,     -0.       ],
                            [      0.    ,     56780.      ,       0.    ,        -0.    ,         0.       ,-284984.498    ],
                            [      0.    ,         0.      ,   56780.    ,         0.    ,    284984.498    ,      0.       ],
                            [      0.    ,        -0.      ,       0.    ,   5141423.444 ,         0.       ,      0.       ],
                            [      0.    ,         0.      ,  284984.498 ,         0.    ,   1430365.6939118,      0.       ],
                            [     -0.    ,   -284984.498   ,       0.    ,         0.    ,         0.       ,1430365.6939118]])
    
        np.testing.assert_almost_equal(StructA.Sft.Mass,56780)
        np.testing.assert_almost_equal(StructA.Sft.r_O.ravel(),(0.23385048,0,89.54857787))
        np.testing.assert_almost_equal(StructA.Sft.MM,Sft_MMref)
        #print('Sft: R_S:')
        #print(StructA.Sft.R_0b)
        #print(StructM.Sft.R_0b)
        #print('Sft: B_S:')
        #print(StructA.Sft.B_inB)
        #print(np.dot(RR,StructM.Sft.B_inB))
        #print(np.dot(RR,StructM.Sft.BB_inB)-StructA.Sft.BB_inB)
        #print(StructA.Sft.Mass)
        #print(StructA.Sft.MM)
        #print(StructA.Sft.r_O)

        # ---  Blade 1
        Bld_MMref = np.array(
                        [[   18035.37974224,       0.          ,     0.        ,       0.        ,  379123.07769825   ,   -0.        ],
                         [       0.        ,   18035.37974224  ,     0.        , -379123.07769825,       0.           ,    0.        ],
                         [       0.        ,       0.          , 18035.37974224,       0.        ,      -0.           ,    0.        ],
                         [       0.        , -379123.07769825  ,     0.        ,12574210.91752538,      -0.           ,   -0.        ],
                         [  379123.07769825,       0.          ,    -0.        ,      -0.        ,12574210.91752538   ,   -0.        ],
                         [      -0.        ,       0.          ,     0.        ,      -0.        ,      -0.           ,    0.        ]])

        np.testing.assert_almost_equal(StructA.Blds[0].Mass,18035.37974224252)
        np.testing.assert_almost_equal(StructA.Blds[0].r_O.ravel(),(-4.67840431,0,90.57868401))
        np.testing.assert_almost_equal(StructA.Blds[0].MM,Bld_MMref)

        np.testing.assert_almost_equal(StructA.Blds[2].Mass,18035.37974224252)
        np.testing.assert_almost_equal(StructA.Blds[2].r_O.ravel(),(-4.67840431,0,90.57868401))
        np.testing.assert_almost_equal(StructA.Blds[2].MM,Bld_MMref)

        #   print(StructA.Blds[0].Mass)
        #   print(StructA.Blds[0].MM)
        #   print(StructA.Blds[0].r_O)
        #     print('Bld1 R_B:')
        #     print(StructA.Blds[0].R_0b)
        #     print(StructM.Blds[0].R_0b)
        #     print('Bld1: B_S:')
        #     print(StructA.Blds[0].B_inB)
        #     print(np.dot(RR,StructM.Blds[0].B_inB))
        #     print(np.dot(RR,StructM.Blds[0].BB_inB)-StructA.Blds[0].BB_inB)
        #     print('Bld2: B_S:')
        #     print(StructM.Blds[1].B_inB)
        #     print(StructA.Blds[1].B_inB)
        # #     print(StructM.Blds[1].BB_inB-StructA.Blds[1].BB_inB)
        #     print('Bld3: B_S:')
        #     print(StructM.Blds[2].B_inB)
        #     print(np.dot(RR,StructA.Blds[2].B_inB ))
        #     print(np.dot(RR,StructM.Blds[2].BB_inB)-StructA.Blds[2].BB_inB)


        #     print('Bld Mass matrix:')
        #     print(StructM.Blds[0].MM[3:,3:])
        #     print(StructA.Blds[0].MM[3:,3:])
        #     print('Bld Mass matrix:')
        #     print(np.dot(RR.T,StructM.Blds[0].MM).dot(RR))
        #     print(StructA.Blds[0].MM-np.dot(RR.T,StructM.Blds[0].MM).dot(RR))
        #     print(np.dot(StructA.Blds[0].BB_inB.T,StructA.Blds[0].MM).dot(StructA.Blds[0].BB_inB))
        #     print(np.dot(StructM.Blds[0].BB_inB.T,StructM.Blds[0].MM).dot(StructM.Blds[0].BB_inB))
        #     print(StructA.Blds[0].MM-StructM.Blds[0].MM)



        # --------------------------------------------------------------------------------}
        # --- Full system
        # --------------------------------------------------------------------------------{
        #     print('Fields available in `Struct`:')
        #     print(Struct.__dict__.keys())

        # --- Damping matrix
        np.testing.assert_almost_equal(StructM.DD,StructA.DD)
        # print('Damp matrix:')
        #print(StructA.DD)
        # print(StructM.DD)
        # print(StructM.DD-StructA.DD)

        # --- Stiff matrix
        KKref = np.array([[2.68290366e+06, 3.90886251e+06, 0.00000000e+00],
                          [3.90886251e+06, 1.46504591e+10, 0.00000000e+00],
                          [0.00000000e+00 , 0.00000000e+00, 0.00000000e+00]])
        np.testing.assert_almost_equal(StructM.KK,StructA.KK)
        np.testing.assert_almost_equal(StructM.KK[:2,:2]/1e6,KKref[:2,:2]/1e6, 4)
        # print('Stiff matrix:')
        # print(StructA.KK)
        # print(StructM.KK-StructA.KK)

        # --- Mass matrix
        MMref=np.array([[  438088.11216229,   744761.80802459,        0.        ],
                        [  744761.80802459, 48008244.21035789,        0.        ],
                        [       0.        ,        0.        , 42635774.95525602]])
        np.testing.assert_almost_equal(StructA.MM,MMref)
        np.testing.assert_almost_equal(StructM.MM,StructA.MM)
        # print('Mass matrix:')
        # print(StructA.MM)
        # print(StructM.MM)
        # print(StructM.MM-StructA.MM)

#         print(StructA.RNA)
#         print(StructM)

    #     print('Origin E :',StructM.Grd.r_O.T)

if __name__=='__main__':
    unittest.main()
