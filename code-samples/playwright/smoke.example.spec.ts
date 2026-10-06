/** Synthetic Playwright example for a demo application. */
import { expect, test } from "@playwright/test";

test("company admin sees limits but cannot access owner-only commercial action", async ({ page }) => {
  await page.goto("http://127.0.0.1:3000/demo/company");

  await expect(page.getByRole("heading", { name: "Company" })).toBeVisible();
  await expect(page.getByText("Approved user seats")).toBeVisible();
  await expect(page.getByRole("button", { name: "Increase commercial limits" })).toHaveCount(0);
});
