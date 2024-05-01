def HTML(dic): 
  return """
<html>
  <body>
    <style>
    .detalles {
  background-color: #ffffff;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.detalles .div {
  background-color: #ffffff;
  border-radius: 71px;
  overflow-x: hidden;
  width: 1013px;
  height: 402px;
  position: relative;
}

.detalles .overlap {
  position: absolute;
  width: 826px;
  height: 402px;
  top: 0;
  left: 158px;
}

.detalles .image {
  width: 55px;
  height: 60px;
  top: 12px;
  left: 771px;
  position: absolute;
  object-fit: cover;
}

.detalles .img {
  width: 200px;
  height: 101px;
  top: 280px;
  left: 582px;
  position: absolute;
  object-fit: cover;
}

.detalles .divisorpunt {
  position: absolute;
  width: 7px;
  height: 402px;
  top: 0;
  left: 523px;
}

.detalles .rectangle {
  position: absolute;
  width: 7px;
  height: 32px;
  top: 0;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .rectangle-2 {
  position: absolute;
  width: 7px;
  height: 32px;
  top: 56px;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .rectangle-3 {
  position: absolute;
  width: 7px;
  height: 32px;
  top: 112px;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .rectangle-4 {
  position: absolute;
  width: 7px;
  height: 32px;
  top: 168px;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .rectangle-5 {
  position: absolute;
  width: 7px;
  height: 32px;
  top: 224px;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .rectangle-6 {
  position: absolute;
  width: 7px;
  height: 32px;
  top: 280px;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .rectangle-7 {
  position: absolute;
  width: 7px;
  height: 32px;
  top: 336px;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .rectangle-8 {
  position: absolute;
  width: 7px;
  height: 10px;
  top: 392px;
  left: 0;
  background-color: #000000;
  border: 1px solid;
  border-color: #d3a867;
}

.detalles .image-2 {
  width: 180px;
  height: 109px;
  top: 3px;
  left: 4px;
  position: absolute;
  object-fit: cover;
}

.detalles .text-wrapper {
  position: absolute;
  width: 215px;
  top: 31px;
  left: 232px;
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 50px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .titfijos {
  position: absolute;
  width: 783px;
  height: 286px;
  top: 57px;
  left: 0;
}

.detalles .text-wrapper-2 {
  position: absolute;
  width: 189px;
  top: 55px;
  left: 0;
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 36px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-3 {
  position: absolute;
  width: 189px;
  top: 0;
  left: 582px;
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 36px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-4 {
  position: absolute;
  width: 189px;
  top: 106px;
  left: 582px;
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 36px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-5 {
  position: absolute;
  width: 232px;
  top: 146px;
  left: 0;
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 36px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-6 {
  position: absolute;
  width: 189px;
  top: 239px;
  left: 0;
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 36px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-7 {
  position: absolute;
  width: 189px;
  top: 239px;
  left: 299px;
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 36px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-8 {
  position: absolute;
  top: 154px;
  left: 0;
  font-family: "Khula", Helvetica;
  font-weight: 600;
  color: #000000;
  font-size: 30px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-9 {
  position: absolute;
  top: 104px;
  left: 582px;
  font-family: "Khula", Helvetica;
  font-weight: 600;
  color: #000000;
  font-size: 30px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-10 {
  position: absolute;
  top: 207px;
  left: 582px;
  font-family: "Khula", Helvetica;
  font-weight: 600;
  color: #000000;
  font-size: 30px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-11 {
  position: absolute;
  width: 340px;
  top: 244px;
  left: 0;
  font-family: "Khula", Helvetica;
  font-weight: 600;
  color: #000000;
  font-size: 18px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-12 {
  left: 2px;
  position: absolute;
  top: 342px;
  font-family: "Khula", Helvetica;
  font-weight: 600;
  color: #000000;
  font-size: 18px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .text-wrapper-13 {
  left: 300px;
  position: absolute;
  top: 342px;
  font-family: "Khula", Helvetica;
  font-weight: 600;
  color: #000000;
  font-size: 30px;
  letter-spacing: 0;
  line-height: normal;
}

.detalles .infotit {
  position: absolute;
  width: 139px;
  height: 402px;
  top: 0;
  left: 0;
}

.detalles .overlap-group {
  position: relative;
  width: 137px;
  height: 402px;
  background-color: #ccecff;
  border-radius: 71px;
}

.detalles .rectangle-9 {
  position: absolute;
  width: 73px;
  height: 402px;
  top: 0;
  left: 64px;
  background-color: #ccecff;
}

.detalles .text-wrapper-14 {
  position: absolute;
  width: 347px;
  top: 160px;
  left: -93px;
  transform: rotate(-90deg);
  font-family: "Khula", Helvetica;
  font-weight: 700;
  color: #000000;
  font-size: 50px;
  letter-spacing: 0;
  line-height: normal;
} """ + f"""
    </style>
    <div class="detalles">
      <div class="div">
        <div class="overlap">
          <img class="image" src="https://c.animaapp.com/APZcOzKZ/img/image-4@2x.png" />
          <img class="img" src="https://c.animaapp.com/APZcOzKZ/img/image-3@2x.png" />
          <div class="divisorpunt">
            <div class="rectangle"></div>
            <div class="rectangle-2"></div>
            <div class="rectangle-3"></div>
            <div class="rectangle-4"></div>
            <div class="rectangle-5"></div>
            <div class="rectangle-6"></div>
            <div class="rectangle-7"></div>
            <div class="rectangle-8"></div>
          </div>
          <img class="image-2" src="https://c.animaapp.com/APZcOzKZ/img/image-2@2x.png" />
          <div class="text-wrapper">AIRLINE</div>
          <div class="titfijos">
            <div class="text-wrapper-2">Código:</div>
            <div class="text-wrapper-3">Latitud:</div>
            <div class="text-wrapper-4">Longitud:</div>
            <div class="text-wrapper-5">Aeropuerto:</div>
            <div class="text-wrapper-6">Ciudad:</div>
            <div class="text-wrapper-7">País:</div>
          </div>
          <div class="text-wrapper-8">{dic.Source_Airport_Code}</div>
          <div class="text-wrapper-9">{dic.Source_Airport_Latitude}</div>
          <div class="text-wrapper-10">{dic.Source_Airport_Longitude}</div>
          <div class="text-wrapper-11">{dic.Source_Airport_Name}</div>
          <div class="text-wrapper-12">{dic.Source_Airport_City}</div>
          <div class="text-wrapper-13">{dic.Source_Airport_Country}</div>
        </div>
        <div class="infotit">
          <div class="overlap-group">
            <div class="rectangle-9"></div>
            <div class="text-wrapper-14">INFORMACIÓN</div>
          </div>
        </div>
      </div>
    </div>
  </body>
</html>
"""