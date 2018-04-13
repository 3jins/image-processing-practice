# 함수 명세
다음과 같이 3개의 함수가 있습니다.

## create_kernel
* input: kernel_size, kernel_type
* output: numpy.array
* 동작
  * kernel_type에 따라 다른 종류의 커널을 반환합니다.
  * kernel_size에 따라 다른 크기의 커널을 반환합니다.
    * 평균값 필터 이외에는 커널사이즈가 7 이상인 경우를 지원하지 않습니다.
    * 커널사이즈가 짝수거나 음수인 경우는 입력을 받지 않습니다.

## apply_kernel
* input: kernel, array, divider
* output: Integer
* 동작
  * 특정 좌표를 포함한 그 주변 좌표값들을 array로 받아 kernel을 적용하여 반환합니다.

## get_smoothed_img
* input: array, kernel, divider, kernel_size
* output: numpy.array
* 동작
  * 이미지의 각 좌표를 순회하며 apply_kernel을 호출합니다.
  * kernel_size에 따라 가장자리의 좌표들은 순회하지 않습니다.


# 사용법

## 필요모듈
* numpy
* Image
* os  

## 사용법
* `python filters.py` 명령어를 통해 실행합니다.
* filters.py와 같은 경로에 sample.jpg 파일이 있어야 합니다.
* 필터링 방법과 커널사이즈를 각각 입력하면 filters.py와 같은 경로에 변환된 이미지파일을 생성합니다.