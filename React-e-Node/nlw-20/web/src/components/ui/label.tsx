'use client';

import { Root as LabelRoot } from '@radix-ui/react-label';
import { type ComponentProps, forwardRef } from 'react';

import { cn } from '../../lib/utils';

const Label = forwardRef<HTMLLabelElement, ComponentProps<typeof LabelRoot>>(
  function LabelComponent({ className, ...props }, ref) {
    return (
      <LabelRoot
        className={cn(
          'flex select-none items-center gap-2 font-medium text-sm leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-50 group-data-[disabled=true]:pointer-events-none group-data-[disabled=true]:opacity-50',
          className
        )}
        data-slot="label"
        ref={ref}
        {...props}
      />
    );
  }
);

export { Label };
