import pygame



def main():
    
    print("Hello World! Suck my stuff")

    running = True

    pygame.init()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print("Key pressed:", event.unicode, end='\r')

                if event.unicode == "q":
                    running = False

    pygame.quit()


if __name__ == "__main__":
    main()