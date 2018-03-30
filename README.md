# embedded-software-practice
건국대 2018년 디지털영상처리 수업 실습과제 코드 저장소입니다.

> **주의**: 혹시나 동기 및 선후배 여러분이 보고 계시다면 실습 pdf에 있는 코드와 구조가 완전히 다른 코드도 있기 때문에 아무 생각없이 베끼면 티 납니다. 참고만 해주세요.



## Homeworks

### 1. 명암대비 조절 

#### 1-1. 단순 조절

* 중간값인 128을 기준으로 128과의 차이만큼에 비례하여 작은 값은 더 작게, 큰 값은 더 크게 만듦.

  ![contrast equation](https://latex.codecogs.com/gif.latex?g%28x%2C%20y%29%20%3D%20f%28x%2C%20y%29%20+%20%28f%28x%2C%20y%29%20-%20128%29%20*%20%5Calpha)

* 0 미만 값과 255 초과 값에 대한 예외처리 필요

#### 1-2. 히스토그램 평활화

- 0~255 각 값에 대한 도수분포 값 획득

  ![histogram equation](https://latex.codecogs.com/gif.latex?h%28g%29%20%3D%20n_g%20%5Cquad%20%280%20%5Cleq%20g%20%5Cleq%20255%29)

- 도수분포를 정규화

  ![normalized histogram equation](https://latex.codecogs.com/gif.latex?p%28g%29%20%3D%20%7Bh%28g%29%20%5Cover%20N%7D%20%5Cquad%5Cquad%5Cquad%20%7B%5Csum_%7Bg%3D0%7D%5E%7B255%7Dp%28g%29%7D%3D1)

- 정규화된 도수분포의 누적분포 획득

  ![accumulated histogram equation](https://latex.codecogs.com/gif.latex?T%28r%29%20%3D%20%5Cint_%7B0%7D%5E%7Br%7Dp_r%28%5Ctau%29d%5Ctau)

  - 여기서는 이산적인 값을 다루므로 정적분 대신 합으로 충분함.
  - 정수가 아닌 경우 반올림

- 이미지의 각 값을 누적분포의 값에 매칭

