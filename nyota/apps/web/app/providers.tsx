// app/providers.tsx
"use client";
import { ThirdwebProvider } from "thirdweb/react";
import { createThirdwebClient } from "thirdweb";
import { base } from "thirdweb/chains";
export const client = createThirdwebClient({ clientId: process.env.NEXT_PUBLIC_THIRDWEB_CLIENT_ID! });
export default ({ children }: { children: React.ReactNode }) =>
  <ThirdwebProvider client={client} activeChain={base}>{children}</ThirdwebProvider>;
