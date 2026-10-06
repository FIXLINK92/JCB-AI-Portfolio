/**
 * Synthetic portfolio example.
 * Demonstrates a commercial-authority boundary without production business logic.
 */

type Role = "OWNER" | "COMPANY_ADMIN" | "USER";

type Limits = Readonly<{
  userSeats: number;
  devices: number;
}>;

type CompanyContext = Readonly<{
  companyId: string;
  role: Role;
  approvedLimits: Limits;
}>;

export function canChangeCommercialLimits(context: CompanyContext): boolean {
  return context.role === "OWNER";
}

export function assertRequestedLimitsWithinApproved(
  context: CompanyContext,
  requested: Limits,
): void {
  if (context.role === "OWNER") return;

  if (
    requested.userSeats > context.approvedLimits.userSeats ||
    requested.devices > context.approvedLimits.devices
  ) {
    throw new Error("Requested limits exceed owner-approved commercial limits");
  }
}

// Example behavior:
const admin: CompanyContext = {
  companyId: "demo-company",
  role: "COMPANY_ADMIN",
  approvedLimits: { userSeats: 25, devices: 10 },
};

assertRequestedLimitsWithinApproved(admin, { userSeats: 20, devices: 8 });
