package com.a304.mozzi.config.security;



import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;

import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import com.fasterxml.jackson.annotation.JsonIgnore;


import java.util.Collection;
import java.util.Collections;


@Builder
@AllArgsConstructor
public class UserPrincipal implements UserDetails {

    @Getter
    private final Integer userId;
    @Getter
    private final String userCode;
    private final Collection<? extends GrantedAuthority> authorities;

    @JsonIgnore
    private final String password;

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return authorities == null ? Collections.emptyList() : authorities;
    }


    @Override
    public String getUsername() {
        return userCode;
    }

    @Override
    public String getPassword() {
        return "$2a$10$2I639JrOZYalstefvnrcK..Xlf8yUY2Opb385BI6plCuNqEAX/50O";
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;
    }

    @Override
    public boolean isEnabled() {
        return true;
    }
}
