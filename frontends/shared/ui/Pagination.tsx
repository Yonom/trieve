import { Accessor } from "solid-js";
import { IoChevronBack, IoChevronForward } from "solid-icons/io";

interface PaginationProps {
  pages: {
    page: Accessor<number>;
    nextPage: () => void;
    prevPage: () => void;
    canGoNext: Accessor<boolean>;
  };
  total?: number;
  perPage?: number;
}
export const Pagination = ({ pages, perPage, total }: PaginationProps) => {
  return (
    <nav
      class="flex items-center justify-between border-t border-gray-200 bg-white py-3 sm:px-6"
      aria-label="Pagination"
    >
      {perPage && total ? (
        <div class="hidden sm:block">
          <p class="text-sm text-gray-700">
            Showing
            <span class="px-1 font-medium">
              {(pages.page() - 1) * perPage || 1}
            </span>
            to
            <span class="px-1 font-medium">
              {(pages.page() - 1) * perPage + perPage}
            </span>
            of
            <span class="px-1 font-medium">{total}</span>
            results
          </p>
        </div>
      ) : null}
      <div class="flex flex-1 justify-between gap-3 sm:justify-end">
        <button
          onClick={() => pages.prevPage()}
          disabled={pages.page() === 1}
          class="relative inline-flex items-center gap-1 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0 disabled:cursor-default disabled:opacity-70 disabled:hover:bg-white"
        >
          <IoChevronBack /> Previous
        </button>
        <button
          onClick={() => pages.nextPage()}
          disabled={!pages.canGoNext()}
          class="relative inline-flex items-center gap-1 rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus-visible:outline-offset-0 disabled:cursor-default disabled:opacity-70 disabled:hover:bg-white"
        >
          Next
          <IoChevronForward />
        </button>
      </div>
    </nav>
  );
};
