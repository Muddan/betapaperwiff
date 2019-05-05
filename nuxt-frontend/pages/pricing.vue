<template>
  <div class="pricing-main">
    <div class="pricing-content">
      <v-container class="subscription-main">
        <div class="header">
          <h1 class="page-title">Pricing Plans</h1>
          <p class="desc">
            Build a permanent home for your writing on a publishing platform
            that grows with you.
          </p>
        </div>
        <v-layout class="price-button-layout">
          <v-flex v-for="(plan, index) in pricingPlans" :key="index" xs12 md4>
            <div class="pricing-card">
              <div class="card-content">
                <div class="card-title">
                  <h4 class="plan-title">{{ plan.title }}</h4>
                  <h3 class="price">{{ plan.price }}</h3>
                  <p class="price-info">{{ plan.info }}</p>
                </div>
                <div class="upgrade-btn">
                  <v-btn round dark large>Upgrade</v-btn>
                </div>
                <p>Details</p>
                <v-expansion-panel v-model="panel" expand inset>
                  <v-expansion-panel-content v-for="(item, i) in 5" :key="i">
                    <template v-slot:header>
                      <div>Item</div>
                    </template>
                    <v-card>
                      <v-card-text
                        >Lorem ipsum dolor sit amet, consectetur adipiscing
                        elit, sed do eiusmod tempor incididunt ut labore et
                        dolore magna aliqua. Ut enim ad minim veniam, quis
                        nostrud exercitation ullamco laboris nisi ut aliquip ex
                        ea commodo consequat.</v-card-text
                      >
                    </v-card>
                  </v-expansion-panel-content>
                </v-expansion-panel>
              </div>
            </div>
          </v-flex>
        </v-layout>
      </v-container>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      panel: [false],
      pricingPlans: [
        {
          title: 'Casual',
          price: '$1/month',
          info: 'billed annually'
        },
        {
          title: 'Pro',
          price: '$6/month',
          info: 'billed monthly or $60 per year'
        },
        {
          title: 'Support',
          price: '$25/month',
          info: 'billed monthly or $250 per year'
        }
      ]
    }
  }
}
</script>

<style lang="scss">
.pricing-main {
  .header {
    width: 100%;
    box-sizing: border-box;
    padding: 20px 20px 0 20px;
    max-width: 1400px;
    margin: auto;
    .page-title {
      color: #2e2e2e;
      text-transform: capitalize;
    }
    .desc {
      font-size: 15px;
      line-height: 2;
      color: #6e6e6e;
    }
  }
  .pricing-content {
    max-width: 1400px;
    margin: auto;
    .price-button-layout {
      flex-wrap: wrap;
    }
    .pricing-card {
      text-align: center;
      margin: 20px 0;
      .card-content {
        box-sizing: border-box;
        padding: 20px 0;
        margin: 0 20px;
        border-radius: 8px;
        background: #e9f2ff;
        box-shadow: 5px 5px 8px 0 #dbdbdb;
      }
      .card-title {
        .plan-title {
          font-size: 36px;
          font-family: 'Marck Script', cursive;
          color: #2e2e2e;
        }
        .price {
          font-size: 20px;
          box-sizing: border-box;
          padding: 10px 0;
        }
        .price-info {
          font-size: 16px;
        }
      }
    }
  }
}
</style>
