// Legacy.h: interface for the Legacy class.
//
//////////////////////////////////////////////////////////////////////

#ifdef WIN32
#pragma warning (disable : 4786)
#endif

#ifndef _LEGACY_H_
#define _LEGACY_H_

#include "bid.h"
#include "normal.h"
#include "BidSet.h"
#include "Param.h"
#include "Distribution.h"

class Legacy : public Distribution {

public:
	char * outputSettings(bool tofile);
	Legacy(Param &p, char * argv[], int argc);
	virtual ~Legacy();

	BidSet *generate(Param &p);
	static void usage();

	void randomizeParams(Param &p);

protected:
	
	double generatePrice(int n, const Param &p);
	int generateNumGoods(Param &p);
	Bid *generateBid(int goods_in_bid, int total_goods, double price);

	Normal *norm;
//	bool printed_usage;

	// distribution parameters
	enum goods_enum {BINOMIAL=1, EXPONENTIAL, RANDOM, CONSTANT, DECAY, NORMAL_GOODS} num_goods_type;
	int const_goods;
	enum pricing_enum {FIXED_RANDOM=1, LINEAR_RANDOM, NORMAL_PRICE, QUADRATIC} pricing_type;

	double binom_cutoff;
	double q;
	double mu_goods;
	double sigma_goods;
	double high_fixed;
	double low_fixed;
	double high_linearly;
	double low_linearly;
	double mu_price;
	double sigma_price;
	double alpha;

	char* output_buffer;
};

#endif
