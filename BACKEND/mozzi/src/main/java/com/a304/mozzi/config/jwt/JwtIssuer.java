package com.a304.mozzi.config.jwt;


import java.time.Instant;
import java.time.temporal.ChronoUnit;
import java.time.Duration;
import java.util.List;

import com.a304.mozzi.config.kakao.KakaoApi;
import com.a304.mozzi.config.kakao.KakaoApi.OAuthToken;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.auth0.jwt.JWT;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.interfaces.DecodedJWT;
//import com.example.restservice.config.kakao.KakaoApi;
//import com.example.restservice.config.kakao.KakaoApi.OAuthToken;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

@Component
//@RequiredArgsConstructor
@Slf4j
public class JwtIssuer {
    @Autowired
    private JwtProperties properties;
//    private final KakaoApi kakaoApi;
//    private final JwtDecoder jwtDecoder;


    public String issue(Integer userId, String email, List<String> roles) {
        return JWT.create()
                .withSubject(String.valueOf(userId))
                .withExpiresAt(Instant.now().plus(Duration.of(1, ChronoUnit.DAYS)))
                .withClaim("e", email)
                .withClaim("a", roles)
                .sign(Algorithm.HMAC256(properties.getSecretKey()));
    }
//
//    public String kakaoIssue(OAuthToken token)
//    {
//        DecodedJWT jwt = jwtDecoder.decode(token.getId_token());
//        return jwt.getPayload();
//    }
}
