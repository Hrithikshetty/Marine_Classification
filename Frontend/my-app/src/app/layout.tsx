import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Component } from "@/components/component/component";
const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "AUTO-FIS",
  description: "MARINE FISH CLASSIFICATION",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body >
      
      {children}
      </body>
      
    </html>
  );
}
