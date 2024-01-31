# 한잔해

* 맞춤형 음료 추천, 광고 시스템
  1. 사람의 성별, 나이, 표정을 인식한 뒤, 추천 AI를 이용해 그에 맞는 음료의 광고를 추천해 준다.
  2. 광고를 보는 사람의 시선을 트래킹한 뒤 광고를 끝까지 시청하면 광고에 나온 음료를 제공한다.
  3. (선택) 음료 시음 후, 음료에 대한 평가를 피드백 받는다.
  4. (Advanced) 피드백한 결과와 사용자의 표정을 데이터로 받아 모델을 학습강화 및 광고사에 결과를 제공한다.

## High Level Design

* usecase
 ![offline customized advertising usecase](https://github.com/chansol1604/project_Ai_ad/assets/145517821/0781a8a6-a40d-484f-965e-cf2484a0370a)

* sequence diagram
 ![sequence](https://github.com/chansol1604/project_Ai_ad/assets/58240527/91651f74-5f6e-4bb2-a9ee-ec11fae0d8ae)


* class diagram
 ![class](https://github.com/chansol1604/project_Ai_ad/assets/58240527/fa44133e-3252-4b91-83bc-3efd578f59bd)


  
## Clone code
```shell
git clone https://github.com/chansol1604/project_Ai_ad.git
```

## Prerequite
* requirements를 이용해 환경 설치
```shell
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

* USB to Serial 통신(USART)를 위해 pyserial 설치
* 시리얼 통신을 하고자 하는 장치가 잘 연결됐는지 확인 및 읽기/쓰기 권한 부여
* openvino 설치 필요 https://docs.openvino.ai/2023.2/openvino_docs_install_guides_installing_openvino_from_archive_linux.html
* open_model_zoo 모델 필요
https://github.com/openvinotoolkit/open_model_zoo 

```shell
sudo pip3 install pyserial

```

## Steps to run

* (프로젝트 실행방법에 대해서 기술, 특별한 사용방법이 있다면 같이 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

cd /project_Ai_ad
source ./run.sh
```

## Output

* ![Screenshot from 2024-01-31 15-38-09](https://github.com/chansol1604/project_Ai_ad/assets/58240527/27b80ff3-bd7e-43ef-9074-55cfd3ea24d1)


* ![Screenshot from 2024-01-31 15-38-20](https://github.com/chansol1604/project_Ai_ad/assets/58240527/1845635c-a1a7-43de-9258-07582d691941)


## Appendix
  0. 데이터셋
   - 김혜경. "연령과 성별에 따른 음식 기호도 조사." (2004).
     
  1. AI 모델
     - 연령, 성별, 감정 인식 모델: 참고 래거시 코드 추가
     - 연령, 성별에 따른 음료 추천 모델: 자체 학습 모델 개발, *********** 폴더 경로 추가 ***************
     - 아이트래킹:
       1) 홍채 원 검출 알고리즘
       https://www.researchgate.net/profile/Kwanggi-Kim/publication/264147873_A_Novel_Circle_Detection_Algorithm_for_Iris_Segmentation/links/5418cc630cf203f155adb6bf/A-Novel-Circle-Detection-Algorithm-for-Iris-Segmentation.pdf
      2) opencv로 얼굴 랜드마크 활용하기
       https://velog.io/@mjkiim_0217/OpenCV-%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%96%BC%EA%B5%B4%EC%9D%B8%EC%8B%9D-%EC%96%B4%EB%85%B8%EC%9E%89-%EC%98%A4%EB%A0%8C%EC%A7%80-%EB%A7%8C%EB%93%A4%EA%B8%B0
      3) 동공 검출 알고리즘
       https://towardsdatascience.com/real-time-eye-tracking-using-opencv-and-dlib-b504ca724ac6
       https://towardsdatascience.com/real-time-eye-tracking-using-opencv-and-dlib-b504ca724ac6

  2. USB to Serial in Linux
     
