// app/checkout/page.tsx
"use client";
import { CheckoutWidget } from "thirdweb/react";
import { client } from "@/app/providers";
import { base } from "thirdweb/chains";
export default function Checkout() {
  return (
    <CheckoutWidget
      client={client}
      chain={base}
      amount="9.99"
      currency="USD"
      seller={process.env.NEXT_PUBLIC_SELLER_ADDRESS!}
      paymentMethods={["card","crypto"]}
      metadata={{ name: "AI Pro Credits", description: "10,000 credits" }}
      onPurchaseSuccess={(evt) => fetch("/api/payments/fulfill",{method:"POST",headers:{"content-type":"application/json"},body:JSON.stringify(evt),credentials:"include"})}
    />
  );
}
