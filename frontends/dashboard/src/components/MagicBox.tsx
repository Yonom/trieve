import { CreateQueryResult } from "@tanstack/solid-query";
import { cva, VariantProps } from "cva";
import { cn } from "shared/utils";
import {
  children,
  createEffect,
  createMemo,
  createSignal,
  JSX,
  Suspense,
} from "solid-js";
import { Show } from "solid-js";

interface MagicBoxProps<D extends CreateQueryResult>
  extends VariantProps<typeof container> {
  class?: string;
  fallback?: JSX.Element;
  id?: string;
  skeletonKey?: string;
  skeletonHeight?: string;
  query: D;
  children: (data: NonNullable<D["data"]>) => JSX.Element;
}

const container = cva([], {
  variants: {
    unstyled: {
      false: "bg-white rounded-md border border-neutral-300 p-4 shadow-sm",
      true: "",
    },
  },
  defaultVariants: {
    unstyled: false,
  },
});

export const MagicBox = <D extends CreateQueryResult>(
  props: MagicBoxProps<D>,
) => {
  const children = createMemo(() => {
    return props.children(props.query.data as NonNullable<D["data"]>);
  });

  const skeletonHeight = createMemo(() => {
    if (props.skeletonKey) {
      if (props.query.status === "success") {
        // save height of div to local storage
        const height = document.getElementById(`skeleton-${props.skeletonKey}`)
          ?.clientHeight;
        if (height) {
          localStorage.setItem(
            `skeleton-${props.skeletonKey}`,
            height.toString(),
          );
        }
      } else {
        // get height from local storage
        const height = localStorage.getItem(`skeleton-${props.skeletonKey}`);
        if (height) {
          return `${height}px`;
        } else {
          return "auto";
        }
      }
    } else {
      if (props.query.isLoading) {
        if (props.skeletonHeight) {
          return `${props.skeletonHeight}px`;
        } else {
          return "auto";
        }
      }
      return "auto";
    }
  });

  return (
    <div
      style={{ height: skeletonHeight() }}
      id={`skeleton-${props.skeletonKey}`}
      class={cn(
        container({ ...props, class: props.class }),
        props.query.isLoading && "unstyled-shimmer",
      )}
    >
      <Show fallback={props.fallback} when={props.query.data}>
        {children()}
      </Show>
    </div>
  );
};

interface MagicSuspenseProps extends VariantProps<typeof container> {
  class?: string;
  fallback?: JSX.Element;
  id?: string;
  skeletonKey?: string;
  skeletonHeight?: string;
  children: JSX.Element;
}

export const MagicSuspense = (props: MagicSuspenseProps) => {
  const [isLoading, setIsLoading] = createSignal(true);
  const skeletonHeight = createMemo(() => {
    if (isLoading() === false) {
      return "auto";
    }
    if (props.skeletonKey) {
      const height = localStorage.getItem(`skeleton-${props.skeletonKey}`);
      return height ? `${height}px` : props.skeletonHeight || "auto";
    }
    return props.skeletonHeight || "auto";
  });

  createEffect(() => {
    if (props.skeletonKey) {
      const element = document.getElementById(`skeleton-${props.skeletonKey}`);
      if (element) {
        const height = element.clientHeight;
        localStorage.setItem(
          `skeleton-${props.skeletonKey}`,
          height.toString(),
        );
      }
    }
  });

  return (
    <div
      style={{ height: skeletonHeight() }}
      id={`skeleton-${props.skeletonKey}`}
      class={cn(container({ ...props, class: props.class }))}
    >
      <Suspense
        fallback={
          props.fallback || <div class="unstyled-shimmer">Loading...</div>
        }
      >
        <>{props.children}</>
      </Suspense>
    </div>
  );
};
