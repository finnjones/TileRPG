            playerSprite = playerSpriteF
            if (bgCam.y - bgCam.height + screenSize[1]) > 0 - 10 or mainPlayer.y != screenSize[1]/2 - 91/2:
                mainPlayer.y += mainPlayer.speed
            else:
                bgCam.y += mainPlayer.speed
                bad1.y -= mainPlayer.speed