"use client"
import React, { useState } from "react";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export function Navbar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleLogout = () => {
    // Perform logout logic
    setIsLoggedIn(false);
  };

  return (
    <header className="bg-black text-white flex gap-4 h-20 w-full items-center px-4 md:px-6">
      <MountainIcon className="w-8 h-8" />
      <span className="text-2xl font-bold text-white">Auto-Fis</span>
      <div className="ml-auto flex gap-2">
        {isLoggedIn ? (
          <Button onClick={handleLogout} variant="outline">
            Log Out
          </Button>
        ) : (
          <Link href="Pages/login">
            <Button variant="outline">Sign Up</Button>
          </Link>
        )}
      </div>
    </header>
  );
}



interface MountainIconProps extends React.SVGProps<SVGSVGElement> {}

function MountainIcon(props: MountainIconProps) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="m8 3 4 8 5-5 5 15H2L8 3z" />
    </svg>
  );
}

export default Navbar;
