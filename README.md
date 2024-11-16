# EwhaGreenCup-Webpage
이화그린컵 프로젝트는 사용자에게 다회용 컵 대여 서비스를 제공하며, 지속 가능한 환경 보호를 실천할 수 있도록 돕기 위해 개발되었습니다. 사용자는 웹 애플리케이션을 통해 컵을 대여하고, 반환 시 스탬프를 획득하여 친환경 활동에 참여할 수 있습니다.

##주요 기술 및 구현
###1. 프론트엔드
HTML/CSS: 사용자 친화적인 UI/UX 디자인.
JavaScript: 지도 표시, 사용자 위치 확인, 실시간 데이터 표시 기능 구현.
Google Maps JavaScript API: 사용자와 대여 위치를 지도에 시각적으로 표시하여 사용자의 편의를 높임.
###2. 백엔드
Django Framework: 웹 애플리케이션 개발에 사용된 프레임워크로 사용자 인증, 데이터베이스 관리 등을 담당.
Django Channels: 실시간 WebSocket 통신을 사용하여 아두이노에서 전송된 위치 데이터를 실시간으로 클라이언트에 전송.
PostgreSQL: 사용자 정보, 대여 기록, 위치 데이터를 안전하게 저장 및 관리.
Redis: Django Channels와 함께 실시간 통신을 위해 사용되는 메시지 브로커.
###3. 아두이노
ESP32 모듈: GPS 모듈과 함께 사용하여 위치 데이터를 수집하고, WiFi 기능을 통해 서버로 전송.
GPS 모듈: 실시간 위치 정보를 정확히 수집.
C++ 코드: 위치 데이터를 읽고 서버로 HTTP 요청을 보내는 기능 구현.


##기능 설명
###1. 홈페이지 소개
![스크린샷 2024-11-16 110310](https://github.com/user-attachments/assets/60ee8122-7419-4563-ae98-a85c3eddc1c6)
사용자는 홈페이지에서 이화그린컵의 개념과 목적에 대해 설명을 볼 수 있습니다.

###2. 회원가입 및 로그인
![스크린샷 2024-11-16 110319](https://github.com/user-attachments/assets/1696eab9-f1c3-482e-af35-d2b5abe6f3fb)
![스크린샷 2024-11-16 110338](https://github.com/user-attachments/assets/660dae0b-effe-4e30-b08a-8a028349fc00)
![스크린샷 2024-11-16 110655](https://github.com/user-attachments/assets/fd9cf43b-8586-4bb5-a40e-c4e6d0a00e77)
![스크린샷 2024-11-16 110705](https://github.com/user-attachments/assets/61ac481e-5967-4d38-82f0-f017b627090b)
새로운 사용자는 회원가입 후 로그인할 수 있으며, 로그인 후 대여 기능을 사용할 수 있습니다.
시범 운영 단계에서의 이화그린컵 도난 방지를 위해 사용자의 정보와 대여, 반환 정보는 저장됩니다.

###3. 대여 및 반환 절차
![스크린샷 2024-11-16 110428](https://github.com/user-attachments/assets/39b874a2-1201-464f-9faa-6dab9968983d)
![스크린샷 2024-11-16 110451](https://github.com/user-attachments/assets/3acc8bad-417c-4746-92f2-f13d32f4736d)
![스크린샷 2024-11-16 110504](https://github.com/user-attachments/assets/c2c5ec2a-bb55-4343-a44f-ba4aa9427ca3)
![스크린샷 2024-11-16 110514](https://github.com/user-attachments/assets/91fe23df-1d04-479b-b2dc-b2232dab2eb3)
![스크린샷 2024-11-16 110532](https://github.com/user-attachments/assets/456635aa-6004-45de-b63b-4c64a0472cc2)
대여: 사용자가 대여 코드를 입력하면 대여가 완료되며, 대여 시작 시간이 기록됩니다.
반환: 사용자가 반환 코드를 입력하면 반환이 완료되고 스탬프가 추가됩니다. 스탬프가 5개 이상 쌓이면 리워드 알림 창이 표시됩니다.

###4. 사용자 위치 및 아두이노 위치 표시(구현중)
![스크린샷 2024-11-16 110554](https://github.com/user-attachments/assets/ac099dae-cd7c-43d9-8d65-0a6f6fb1942f)
웹페이지에 사용자의 현재 위치와 아두이노에서 제공하는 대여 위치가 지도에 표시됩니다. 이를 통해 사용자는 수거함의 위치를 실시간으로 확인할 수 있습니다.

###5. 그 외 기능
![스크린샷 2024-11-16 110542](https://github.com/user-attachments/assets/9d65cc75-b588-4b65-86b8-f0ed360f1826)
자판기 및 RC카 관리를 위한 긴급 연락처를 추가하였습니다.

##보안 및 데이터 보호
환경 변수 사용: 프로젝트 설정에서 민감한 데이터(예: API 키, 데이터베이스 비밀번호)는 환경 변수로 관리하여 보안성을 높였습니다.
HTTPS: 배포 시 보안을 위해 HTTPS 프로토콜을 사용하여 사용자 데이터 전송을 암호화할 수 있습니다.

##프로젝트 개선점 및 추가 기능
향후 모바일 앱과 연동하여 더 편리한 사용자 경험을 제공할 계획.
추가적인 푸시 알림 기능을 통해 대여 및 반환 시 사용자 알림 서비스 구현.
