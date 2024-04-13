import { For, Match, Show, Switch, createMemo } from "solid-js";
import { createEffect, createSignal, onCleanup } from "solid-js";
import {
  OrganizationAndSubAndPlan,
  StripePlan,
  StripeSubscription,
} from "../types/apiTypes";
import { BsCheck } from "solid-icons/bs";
import {
  formatBytesDecimal,
  numberFormatter,
  usdFormatter,
} from "../formatters";
import { AiOutlineWarning } from "solid-icons/ai";
import { createToast } from "./ShowToasts";

export interface PlansTableProps {
  currentOrgSubPlan: OrganizationAndSubAndPlan | null;
}

const activeTag = (text: string) => {
  return (
    <p class="w-fit rounded-lg bg-neutral-100 px-4 py-2 font-semibold text-magenta-500 shadow-sm shadow-magenta-100/40">
      {text}
    </p>
  );
};

export const PlansTable = (props: PlansTableProps) => {
  const api_host = import.meta.env.VITE_API_HOST as unknown as string;

  const [availablePlans, setAvailablePlans] = createSignal<StripePlan[]>([]);
  const [currentPlan, setCurrentPlan] = createSignal<StripePlan | null>(null);
  const [currentSubscription, setCurrentSubscription] =
    createSignal<StripeSubscription | null>(null);
  const [processingPlanId, setProcessingPlanId] = createSignal<string | null>(
    null,
  );
  const [canceling, setCanceling] = createSignal(false);

  createEffect(() => {
    console.log("props.currentOrgSubPlan", props.currentOrgSubPlan);

    setCurrentPlan(props.currentOrgSubPlan?.plan ?? null);
    setCurrentSubscription(props.currentOrgSubPlan?.subscription ?? null);
  });

  createEffect(() => {
    const availablePlansAbortController = new AbortController();
    void fetch(`${api_host}/stripe/plans`, {
      credentials: "include",
      headers: {
        "TR-Organization": props.currentOrgSubPlan?.organization.id ?? "",
      },
      signal: availablePlansAbortController.signal,
    })
      .then((res) => res.json())
      .then((data) => {
        setAvailablePlans(
          (data as StripePlan[]).sort((a, b) => a.amount - b.amount),
        );
      });

    onCleanup(() => {
      availablePlansAbortController.abort();
    });
  });

  const availablePlansWithCurrent = createMemo(() => {
    const curPlan = currentPlan();
    const curSub = currentSubscription();

    const availablePlansList = availablePlans();
    const availablePlansWithCurrent = availablePlansList.map((plan) => {
      return {
        ...plan,
        current: plan.id === curPlan?.id,
        current_period_end: curSub?.current_period_end,
      };
    });

    return availablePlansWithCurrent;
  });

  const refetchOrgSubPlan = async () => {
    const selectedOrgId = props.currentOrgSubPlan?.organization.id ?? "";

    const resp = await fetch(`${api_host}/organization/${selectedOrgId}`, {
      credentials: "include",
      headers: {
        "TR-Organization": selectedOrgId,
      },
    });

    if (resp.ok) {
      const data = (await resp.json()) as OrganizationAndSubAndPlan;
      setCurrentSubscription(data.subscription ?? null);
      setCurrentPlan(data.plan ?? null);
    }
  };

  const cancelPlan = async () => {
    setCanceling(true);
    await fetch(
      `${api_host}/stripe/subscription/${
        props.currentOrgSubPlan?.subscription?.id ?? ""
      }`,
      {
        credentials: "include",
        method: "DELETE",
        headers: {
          "TR-Organization": props.currentOrgSubPlan?.organization.id ?? "",
        },
      },
    );

    await new Promise((resolve) => setTimeout(resolve, 500));

    await refetchOrgSubPlan();
    createToast({ title: "Subscription canceled", type: "success" });
    setCanceling(false);
  };

  const updatePlan = async (plan: StripePlan) => {
    setProcessingPlanId(plan.id);

    const resp = await fetch(
      `${api_host}/stripe/subscription_plan/${
        props.currentOrgSubPlan?.subscription?.id ?? ""
      }/${plan.id}`,
      {
        credentials: "include",
        method: "PATCH",
        headers: {
          "TR-Organization": props.currentOrgSubPlan?.organization.id ?? "",
        },
      },
    );

    if (resp.ok) {
      setCurrentPlan(plan);
      createToast({
        title: `Subscription changed to ${plan.name}`,
        type: "success",
      });
      setProcessingPlanId(null);
    }

    void refetchOrgSubPlan();
  };

  return (
    <div>
      <div class="grid w-full grid-cols-3 place-content-center gap-x-2 rounded bg-neutral-100 p-3 text-sm">
        <div class="space-y-1">
          <p class="text-lg uppercase text-magenta-500">Enterprise</p>
          <p>
            For applications managing serious workloads. Signal, WhatsApp, or
            Telegram all work.
          </p>
          <a
            class="block rounded bg-magenta-100 py-1 text-center"
            href="tel:6282224090"
          >
            +1 628-222-4090
          </a>
          <a class="block text-center text-xs" href="mailto:humans@trieve.ai">
            humans@trieve.ai
          </a>
        </div>
        <div class="mx-auto my-auto space-y-2">
          <div class="flex items-center space-x-2">
            <BsCheck class="fill-current text-magenta-500" />
            <p> 24x7x365 Dedicated Support </p>
          </div>
          <div class="flex items-center space-x-2">
            <BsCheck class="fill-current text-magenta-500" />
            <p> SLAs / DPAs / MSAs </p>
          </div>
          <div class="flex items-center space-x-2">
            <BsCheck class="fill-current text-magenta-500" />
            <p> On-premise support </p>
          </div>
        </div>
        <div class="mx-auto my-auto space-y-2">
          <div class="flex items-center space-x-2">
            <BsCheck class="fill-current text-magenta-500" />
            <p> Provider VPC peering </p>
          </div>
          <div class="flex items-center space-x-2">
            <BsCheck class="fill-current text-magenta-500" />
            <p> SSO/SAML </p>
          </div>
          <div class="flex items-center space-x-2">
            <BsCheck class="fill-current text-magenta-500" />
            <p> 24x7x365 support </p>
          </div>
        </div>
      </div>
      <div class="mt-10 space-y-4">
        <h3 class="text-lg font-semibold text-neutral-800">
          Change subscription plan for{" "}
          {props.currentOrgSubPlan?.organization.name} Organization
        </h3>
        <Show when={currentSubscription()?.current_period_end}>
          {(end_date_str) => (
            <div class="flex space-x-2 bg-yellow-50 px-4 py-2">
              <AiOutlineWarning class="block fill-current pt-1 text-yellow-500" />
              <div>
                <p class="font-semibold text-yellow-800">Notice</p>
                <p class="text-sm">
                  This organization will lose the{" "}
                  <span
                    class="font-semibold
  "
                  >
                    {currentPlan()?.name}
                  </span>{" "}
                  plan benefits on{" "}
                  {new Date(end_date_str()).toLocaleDateString()} and be
                  downgraded to the Free plan.
                </p>
              </div>
            </div>
          )}
        </Show>
        <div class="overflow-hidden rounded shadow ring-1 ring-black ring-opacity-5">
          <table class="min-w-full divide-y divide-neutral-300">
            <thead class="bg-neutral-100">
              <tr>
                <th
                  scope="col"
                  class="py-3.5 pl-4 text-left text-sm font-semibold sm:pl-6"
                >
                  Name
                </th>
                <th
                  scope="col"
                  class="px-3 py-3.5 text-left text-sm font-semibold"
                >
                  Price
                </th>
                <th
                  scope="col"
                  class="px-3 py-3.5 text-left text-sm font-semibold"
                >
                  Chunks
                </th>
                <th
                  scope="col"
                  class="px-3 py-3.5 text-left text-sm font-semibold"
                >
                  Users
                </th>
                <th
                  scope="col"
                  class="px-3 py-3.5 text-left text-sm font-semibold"
                >
                  Datasets
                </th>
                <th
                  scope="col"
                  class="px-3 py-3.5 text-left text-sm font-semibold"
                >
                  Storage
                </th>
                <th
                  scope="col"
                  class="px-3 py-3.5 text-left text-sm font-semibold"
                >
                  Gen AI Messages
                </th>
                <th scope="col" class="px-3 py-3.5" />
              </tr>
            </thead>
            <tbody class="divide-y divide-neutral-200 bg-white">
              <tr>
                <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium sm:pl-6">
                  FREE
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                  {usdFormatter.format(0)}/mo
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                  {numberFormatter.format(1000)}
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                  {numberFormatter.format(1)}
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                  {numberFormatter.format(1)}
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                  {formatBytesDecimal(500000000)}
                </td>
                <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                  {numberFormatter.format(500)}
                </td>
                <td
                  classList={{
                    "whitespace-nowrap px-3 py-4": true,
                    "animate-pulse": canceling(),
                  }}
                >
                  <Switch>
                    <Match when={currentPlan()?.amount === 0}>
                      {activeTag("Current Tier")}
                    </Match>
                    <Match
                      when={
                        currentSubscription()?.current_period_end &&
                        currentPlan()?.amount !== 0
                      }
                    >
                      {activeTag(
                        "Starts on " +
                          new Date(
                            currentSubscription()?.current_period_end ?? "",
                          ).toLocaleDateString(),
                      )}
                    </Match>
                    <Match when={currentPlan()?.amount !== 0}>
                      <button
                        onClick={() => {
                          void cancelPlan();
                        }}
                        class="w-fit rounded-lg bg-magenta-500 px-4 py-2 font-semibold text-white shadow-sm shadow-magenta-100/40"
                      >
                        Downgrade to Free (Cancel)
                      </button>
                    </Match>
                  </Switch>
                </td>
              </tr>
              <For each={availablePlansWithCurrent()}>
                {(plan) => {
                  const curPlan = currentPlan();
                  const isUpgrade = curPlan
                    ? curPlan.amount < plan.amount
                    : false;

                  const currentPeriodEnd = plan.current_period_end;
                  let actionButton = activeTag("Current Tier");

                  if (!plan.current || currentPeriodEnd) {
                    if ((curPlan?.amount ?? 0) > 0 && !currentPeriodEnd) {
                      const onClickFunc = () => {
                        void updatePlan(plan);
                      };
                      const buttonText = isUpgrade ? "Upgrade" : "Downgrade";
                      actionButton = (
                        <button
                          onClick={onClickFunc}
                          classList={{
                            "w-fit px-4 py-2 bg-magenta-500 text-white font-semibold rounded-lg shadow-sm shadow-magenta-100/40":
                              true,
                            "animate-pulse cursor-not-allowed":
                              processingPlanId() === plan.id,
                          }}
                        >
                          {buttonText}
                        </button>
                      );
                    } else {
                      actionButton = (
                        <a
                          href={`${api_host}/stripe/payment_link/${plan.id}/${props.currentOrgSubPlan?.organization.id}`}
                          class="w-fit rounded-lg bg-magenta-500 px-4 py-2 font-semibold text-white shadow-sm shadow-magenta-100/40"
                        >
                          Subscribe
                        </a>
                      );
                    }
                  }

                  return (
                    <tr>
                      <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium sm:pl-6">
                        {plan.name}
                      </td>
                      <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                        {usdFormatter.format(plan.amount / 100)}/mo
                      </td>
                      <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                        {numberFormatter.format(plan.chunk_count)}
                      </td>
                      <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                        {numberFormatter.format(plan.user_count)}
                      </td>
                      <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                        {numberFormatter.format(plan.dataset_count)}
                      </td>
                      <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                        {formatBytesDecimal(plan.file_storage)}
                      </td>
                      <td class="whitespace-nowrap px-3 py-4 text-sm text-neutral-800">
                        {numberFormatter.format(plan.message_count)}
                      </td>
                      <td class="whitespace-nowrap px-3 py-4">
                        {actionButton}
                      </td>
                    </tr>
                  );
                }}
              </For>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
