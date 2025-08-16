// app/(auth)/sign-in/page.tsx
"use client";
import { ConnectButton } from "thirdweb/react";
import { client } from "@/app/providers";
export default function SignIn() {
  return (
    <ConnectButton
      client={client}
      auth={{
        getLoginPayload: async (p) => (await fetch("/api/auth/payload",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(p),credentials:"include"})).json(),
        doLogin: async (params) => fetch("/api/auth/login",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(params),credentials:"include"}),
        isLoggedIn: async () => (await (await fetch("/api/auth/is-logged-in",{credentials:"include"})).json()).loggedIn,
        doLogout: async () => fetch("/api/auth/logout",{method:"POST",credentials:"include"}),
      }}
    />
  );
}
