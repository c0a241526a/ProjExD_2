import os
import sys
import random
import pygame as pg


WIDTH, HEIGHT = 1100, 650
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DELTA={ #  移動量辞書　辞書(dict)は{}で作る
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,+5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(+5,0),
    }


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 0.9)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300, 200
    bb_img=pg.Surface((20,20))  # 空のSurfaceを作成
    bb_img.set_colorkey((0, 0, 0))  # 黒色を透明に設定
    pg.draw.circle(bb_img, (255, 0, 0), (10, 10), 10)  # circle(引数：描画用Surface，色，中心座標，半径)で円作成 
    bb_rct = bb_img.get_rect()  # 爆弾rectを取得
    bb_rct.centerx=random.randint(0,WIDTH)  # 乱数から爆弾の初期配置(横座標) 
    bb_rct.centery=random.randint(0,HEIGHT)   # 乱数から爆弾の初期配置(縦座標) 
    vx,vy=+5,+5  # 爆弾の移動速度
    clock = pg.time.Clock()
    tmr = 0
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 

        key_lst = pg.key.get_pressed()  # キー押したとき
        sum_mv = [0, 0]
        for key, mv in DELTA.items():  # items()で辞書の二つの内容をそれぞれkeyとmvにとれる
            if key_lst[key]:
                sum_mv[0]+=mv[0]
                sum_mv[1]+=mv[1]
        #if key_lst[pg.K_UP]:
        #    sum_mv[1] -= 5
        #if key_lst[pg.K_DOWN]:
        #    sum_mv[1] += 5
        #if key_lst[pg.K_LEFT]:
        #    sum_mv[0] -= 5
        #if key_lst[pg.K_RIGHT]:
        #    sum_mv[0] += 5
        kk_rct.move_ip(sum_mv)
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)  # 爆弾の移動
        screen.blit(bb_img, bb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
