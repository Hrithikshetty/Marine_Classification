import React from "react";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export function Navbar() {
  return (
    <header className="flex h-20 w-full items-center px-4 md:px-6">
      <div className="ml-auto flex gap-2">
        <Link href="Pages/login">
            <Button variant="outline">Sign in</Button>
        </Link>
      </div>
    </header>
  );
}

export default Navbar;
