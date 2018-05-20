import Animals

def main():
    cocoInfo = Animals.am.Info()
    cocoInfo.type = "Pomeranian"
    cocoInfo.height = 7
    cocoInfo.weight = 12
    cocoInfo.age = 2

    coco = Animals.Dog("Coco", cocoInfo)
    coco.doAction()


    naviInfo = Animals.am.Info()
    naviInfo.type = "Pomeranian"
    naviInfo.height = 7
    naviInfo.weight = 12
    naviInfo.age = 2

    navi = Animals.Cat("Navi", naviInfo)
    navi.doAction()


if __name__ == "__main__":
    main()
