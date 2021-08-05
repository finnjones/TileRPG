    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        if bgCam.y < 0 + 10 or mainPlayer.y > screenSize[1]/2 - 91/2:
            mainPlayer.y -= mainPlayer.speed
        else:
            bgCam.y -= mainPlayer.speed

    if keys[pygame.K_s]:

        if (bgCam.y - bgCam.height + screenSize[1]) > 0 or mainPlayer.y != screenSize[1]/2 - 91/2:
            mainPlayer.y += mainPlayer.speed
        else:
            bgCam.y += mainPlayer.speed

    if keys[pygame.K_d]:
        if (bgCam.x - bgCam.height + screenSize[0]) > 0 or mainPlayer.x != screenSize[0]/2 - 100/2:
            mainPlayer.x += mainPlayer.speed
        else:
            bgCam.x += mainPlayer.speed

    if keys[pygame.K_a]:
        if bgCam.x < 0 + 10 or mainPlayer.x != screenSize[0]/2 - 100/2:
            mainPlayer.x -= mainPlayer.speed
        else:
            bgCam.x -= mainPlayer.speed