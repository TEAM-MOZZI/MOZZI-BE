import React, { useEffect, useRef } from 'react';
import { Animated, TouchableOpacity, Image, Text } from 'react-native';
import styled from 'styled-components/native';
import axios from 'axios';

import { useNavigation } from '@react-navigation/native';
import KakaoLogins, {login as kakaoLoginFunc, getProfile} from '@react-native-seoul/kakao-login';
import useLoginStore from '../../store/LoginStore';

import kakao from '../../assets/landing/kakao-login-icon.png';
import wave from '../../assets/landing/wave-bg.png';

const icons = [
  require('../../assets/landing/icon1.png'),
  require('../../assets/landing/icon2.png'),
  require('../../assets/landing/icon3.png'),
  require('../../assets/landing/icon4.png'),
  require('../../assets/landing/icon5.png'),
  require('../../assets/landing/icon6.png'),
  require('../../assets/landing/icon7.png'),
  require('../../assets/landing/icon8.png'),
  require('../../assets/landing/icon9.png'),
];

const Container = styled.View`
  flex: 1;
  background-color: #FFFDD4;
`;

const AnimatedBgImg = Animated.createAnimatedComponent(styled.Image`
  position: absolute;
  width: 100%;
  height: 80%;
  top: -15%;
`);

const AnimatedFoodIcon = Animated.createAnimatedComponent(styled.Image`
  position: absolute;
  width: ${props => props.width}px;
  height: ${props => props.height}px;
  top: ${props => props.top}px;
  left: ${props => props.left}px;
`);

const TitleContainer = styled.View`
  position: absolute;
  margin-top: 20%;
  padding-left: 15%;
`;

const SmallTitle = styled(Text)`
  font-family: ${(props) => props.theme.fonts.landing};
  font-size: 48px;
  color: ${(props) => props.theme.palette.main};;
`;

const BigTitle = styled(Text)`
  font-family: ${(props) => props.theme.fonts.landing};
  font-size: 96px;
  color: ${(props) => props.theme.palette.main};
`;

const LoginContainer = styled.View`
  position: absolute;
  bottom: 22%;
  width: 100%;
  align-items: center;
`;

const AnimatedLoginButton = Animated.createAnimatedComponent(TouchableOpacity);

function LandingScreen() {
  const navigation = useNavigation();
  const { login: storeLogin, userData } = useLoginStore()

  const kakaoLogin = async () => {
    console.log("테스팅 중")
    try {
      // 여기에서 함수 이름을 kakaoLoginFunc로 변경했습니다.
      const res = await kakaoLoginFunc();
      console.log('로그인 성공!:', JSON.stringify(res));
      console.log(res); // 반환되는 객체 확인
      // accessToken을 전달하기 전에 res가 정상인지 확인
      if (res) {
        // 성공적으로 토큰을 받아오고 로그인 처리
        await storeLogin(res.idToken);

        // 로그인 후 LandingInputScreen으로 이동
        navigation.navigate('LandingInput');
        
      } else {
        console.log('Login response is undefined');
      }
    } catch (error) {
      if (error.code === 'E_CANCELLED_OPERATION') {
        console.log('Login cancelled')
      } else {
        console.error(error)
      }
    }
  }
  
  // const signInWithKakao = async (): Promise<void> => {
  //   try {
  //     const token = await kakaoLoginFunc();
  //     setResult(JSON.stringify(token));
  //   } catch (err) {
  //     console.error('login err', err);
  //   }
  // };

  // // 테스트 코드
  // const sendRequest = async () => {
  //   try {
  //     const response = await axios.get('https://a304.site/api/mozzi/test');
  //     console.log('성공:', response.data);
  //   } catch (error) {
  //     console.error('에러:', error);
  //   }
  // };  
  // // sendRequest 함수 호출
  // sendRequest();

  // const fadeAnims = useRef(
  //   Array.from({ length: 9 }, () => new Animated.Value(0))
  // ).current;

  // 각 아이콘과 로그인 버튼에 대한 페이드인 애니메이션 값
  const fadeAnims = useRef(icons.map(() => new Animated.Value(0))).current;
  const loginFadeAnim = useRef(new Animated.Value(0)).current;

  // 페이드인 애니메이션을 시작하는 함수
  const fadeIn = (animValue, delay) => {
    Animated.timing(animValue, {
      toValue: 1,
      duration: 1000,
      delay,
      useNativeDriver: true,
    }).start();
  };

  useEffect(() => {
    // 아이콘 애니메이션
    fadeAnims.forEach((anim, index) => {
      fadeIn(anim, index * 500); // 각 아이콘이 0.5초 간격으로 나타나게 설정
    });

    // 모든 아이콘 애니메이션 후 로그인 버튼 애니메이션 시작
    const lastIconDelay = icons.length * 500;
    fadeIn(loginFadeAnim, lastIconDelay);
  }, []);


  // 위치와 크기 정보
  const positions = [
    { width: 53, height: 53, top: 334.82, left: 77 },
    { width: 64, height: 64, top: 361.72, left: 179 },
    { width: 65, height: 65, top: 270, left: 286 },
    { width: 66, height: 66, top: 442.42, left: 44 },
    { width: 50, height: 50, top: 529.09, left: 190 },
    { width: 67, height: 67, top: 467.32, left: 290 },
    { width: 58, height: 58, top: 765.21, left: 53 },
    { width: 65, height: 65, top: 707.43, left: 149 },
    { width: 80, height: 80, top: 742.3, left: 277 },
  ];

  return (
    <Container>
      <AnimatedBgImg source={wave} style={{ opacity: fadeAnims[0] }} />
      <TitleContainer>
        <SmallTitle>오늘 모 먹찌?</SmallTitle>
        <BigTitle>모찌</BigTitle>
      </TitleContainer>

      {/* 아이콘들을 순회하며 AnimatedFoodIcon 컴포넌트 생성 */}
      {positions.map((pos, index) => (
        <AnimatedFoodIcon
          key={index}
          source={icons[index]}
          style={[
            {
              width: pos.width,
              height: pos.height,
              top: pos.top,
              left: pos.left,
              opacity: fadeAnims[index],
            },
          ]}
        />
      ))}

      <LoginContainer>
      {/* 로그인 버튼 */}
        <AnimatedLoginButton
          style={{ opacity: loginFadeAnim }}
          onPress={kakaoLogin}
        >
          <Image source={kakao} />
        </AnimatedLoginButton>
      </LoginContainer>
    </Container>
  );
}

export default LandingScreen;
