import { useContext } from "solid-js";
import { ProgressBar } from "./ProgressBar";
import { formatNumberWithCommas, formatStorage } from "../utils/formatNumbers";
import { createQuery } from "@tanstack/solid-query";
import { UserContext } from "../contexts/UserContext";
import { ApiContext } from "..";
import { OrganizationAndSubAndPlan } from "shared/types";

export const OrganizationUsageOverview = () => {
  const userContext = useContext(UserContext);
  const trieve = useContext(ApiContext);

  const usageQuery = createQuery(() => ({
    queryKey: ["org-usage", userContext.selectedOrg().id],
    queryFn: async () => {
      return trieve.fetch("/api/organization/usage/{organization_id}", "get", {
        organizationId: userContext.selectedOrg().id,
      });
    },
  }));

  const subscriptionQuery = createQuery(() => ({
    queryKey: ["org-subscription", userContext.selectedOrg().id],
    queryFn: async () => {
      return trieve.fetch<"eject">(
        "/api/organization/{organization_id}",
        "get",
        {
          organizationId: userContext.selectedOrg().id,
        },
      ) as Promise<OrganizationAndSubAndPlan>;
    },
  }));

  return (
    <div class="mb-3 grid grid-cols-1 gap-5 lg:grid-cols-4">
      <dl class="col-span-4 grid grid-cols-1 divide-y divide-gray-200 overflow-hidden rounded-lg border bg-white shadow md:grid-cols-2 md:divide-x md:divide-y-0">
        <div class="px-4 py-5 sm:p-6">
          <dt class="text-base font-normal"> Total Users </dt>
          <dd class="mt-1 flex items-baseline justify-between md:block lg:flex">
            <div class="flex items-baseline text-2xl font-semibold text-magenta">
              {formatNumberWithCommas(usageQuery.data?.user_count ?? 0)}
              <span class="ml-2 text-sm font-medium text-neutral-600">
                of
                {formatNumberWithCommas(
                  subscriptionQuery.data?.plan?.user_count || 0,
                )}
              </span>
            </div>
          </dd>
        </div>
        <div class="px-4 py-5 sm:p-6">
          <dt class="text-base font-normal">Total File Storage</dt>
          <dd class="mt-1 flex items-baseline justify-between md:block lg:flex">
            <div class="flex flex-col items-baseline gap-3 text-2xl font-semibold text-magenta">
              <div>
                {formatNumberWithCommas(usageQuery.data?.file_storage ?? 0)} mb
                <span class="ml-2 text-sm font-medium text-neutral-600">
                  of{" "}
                  {formatStorage(
                    subscriptionQuery.data?.plan?.file_storage || 0,
                  )}{" "}
                </span>
              </div>
              <ProgressBar
                width={"200px"}
                max={subscriptionQuery.data?.plan?.file_storage || 0}
                progress={usageQuery.data?.file_storage || 0}
              />
            </div>
          </dd>
        </div>
        <div class="px-4 py-5 sm:p-6">
          <dt class="text-base font-normal">Total Message Count</dt>
          <dd class="mt-1 flex items-baseline justify-between md:block lg:flex">
            <div class="flex flex-col items-baseline gap-3 text-2xl font-semibold text-magenta">
              <div>
                {formatNumberWithCommas(usageQuery.data?.message_count ?? 0)}
                <span class="ml-2 text-sm font-medium text-neutral-600">
                  of{" "}
                  {formatNumberWithCommas(
                    subscriptionQuery.data?.plan?.message_count ?? 0,
                  )}
                </span>
              </div>
              <ProgressBar
                width={"200px"}
                max={subscriptionQuery.data?.plan?.message_count || 0}
                progress={usageQuery.data?.message_count || 0}
              />
            </div>
          </dd>
        </div>
        <div class="px-4 py-5 sm:p-6">
          <dt class="text-base font-normal">Total Chunk Count</dt>
          <dd class="mt-1 flex items-baseline justify-between md:block lg:flex">
            <div class="flex flex-col items-baseline gap-3 text-2xl font-semibold text-magenta">
              <div>
                {formatNumberWithCommas(usageQuery.data?.chunk_count ?? 0)}
                <span class="ml-2 text-sm font-medium text-neutral-600">
                  of{" "}
                  {formatNumberWithCommas(
                    subscriptionQuery.data?.plan?.chunk_count ?? 0,
                  )}
                </span>
              </div>
              <ProgressBar
                width={"200px"}
                max={subscriptionQuery.data?.plan?.chunk_count || 0}
                progress={usageQuery.data?.chunk_count || 0}
              />
            </div>
          </dd>
        </div>
      </dl>
    </div>
  );
};